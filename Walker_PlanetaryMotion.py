'''
Author: Walker Laitala
Date Created: 2/7/2024
Date Updated: 2/24/2024

Description: Program that plots the orbital motion of any mass around another in space given initial values, with some bells and whistles
Bugs: I am running out of visual studio, and it only runs if you click ...>Run>Run Without Debugging. It does not run for some reason if you click the arrow in the top right corner. 

Basically what you are looking at: 
    There are two main functions, one (live) that graphs an animation of a mass orbiting another mass in space. You can change the initial values below to 
test out different planets or asteroids or satellites or whatever orbiting bodies you want. It is currently set to Earth around Sun with the Moon simultaneously orbiting the Earth. 
Note that the orbiting distance of the Moon around the Earth is exaggerated by 25x because otherwise you can't tell them apart. 

    The second function, static, graphs a still image of one period of a mass's orbit around another mass. It is currently set to Mercury around the Sun because that is our Solar System's most elliptical orbit. 
The goal of this is to prove Kepler's 2nd Law of Planetary Motion, that planets sweep out in equal areas in equal times. The graph will also have multiple polygons that represent the area travelled by the 
planet in a fixed amount of time. This area is approximated by an infinitely-sided polygon (you can give it as many vertices as you want). If Kepler's 2nd Law is true, all the polygons should be the same area, 
as long as their orbiting sections are the same amount of time. The second graph that pops up shows the area of the different polygons as their number of vertices increase. They all approach the same number, which means
Kepler's 2nd Law is true. You can play around with the initial orbital values as well as however many polygons you want, what their max vertices should be, and how far the 
orbit secions should be, and all that fun stuff.

Choose which function to run at the very bottom by unhiding whichever function you want and hiding the other.

All initial values are sourced from NASA and the orbits of the bodies come from Newton's Law of Universal Gravitation.
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from tqdm import tqdm
import math

#THESE INITIALS ARE ONLY FOR "LIVE" FUNCTION
#Moon around Earth Initials     Note on variable names - Mp_y refers to "moon position y", while Ev_x refers to "earth velocity x" etc. 
G = 6.67e-11                #univeral gravitational constant
Mass_Earth = 5.97e24        #kg
Mp_x = 3.84e8               #m
Mp_y = 0
Mv_x = 0
Mv_y = 1022                 #m/s
Mxs = [Mp_x]                #list of all the different x coordinates of orbit
Mys = [Mp_y]                #list of all the different y coordinates of orbit

#Earth Around Sun Initials FOR LIVE
Mass_Sun = 1.9891e30        #kg
Ep_x = 1.5e11               #m
Ep_y = 0
Ev_x = 0
Ev_y = 29784                #m/s
Exs = [Ep_x]                #list of all the different x coordinates of orbit
Eys = [Ep_y]                #list of all the different y coordinates of orbit

#Time Conditions FOR LIVE
delta_time = 5000           #How much time elapses between datapoints
time_increments = 40        #how many data points are graphed in a frame              These two simply control the speed of the animation

fig, ax = plt.subplots()    #defining fig and ax as plots for the remainder of program

def shoelace_formula(polygonBoundary, absoluteValue = True):        #function that calculates the area of a polynomial using Gauss's area formula
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2.)
    else:
        return sum(l) / 2.

def live():                 #animated visualization of earth orbiting around sun while moon orbits around earth

    def animate(i):         #function for animation

        global Mp_x         #making all the initial conditions global
        global Mp_y
        global Mv_x
        global Mv_y
        global Mxs
        global Mys
        global Mass_Earth

        global Ep_x
        global Ep_y
        global Ev_x
        global Ev_y
        global Exs
        global Eys
        global Mass_Sun

        global delta_time
        global time_increments

        ax.clear()          #clears the plot, otherwise things will get messy fast
        
        #Moon Around Earth
        for z in range(time_increments):        #tqdm() ?

            Ea_x = (-G*Mass_Sun*Ep_x)/((Ep_x**2 + Ep_y**2)**1.5)        #equation for calculating the acceleration of earth
            Ea_y = (-G*Mass_Sun*Ep_y)/((Ep_x**2 + Ep_y**2)**1.5)

            Ev_x = Ev_x + Ea_x*delta_time       #equation for velocities of earth
            Ev_y = Ev_y + Ea_y*delta_time

            Ep_x = Ep_x + delta_time*Ev_x       #equation for positions of earth
            Ep_y = Ep_y + delta_time*Ev_y

            Exs.append(Ep_x)                    #add the new x/y positions to their respective lists
            Eys.append(Ep_y)
            
            Ma_x = (-G*Mass_Earth*Mp_x)/((Mp_x**2 + Mp_y**2)**1.5)      #same thing - acceleration calcs, but for moon
            Ma_y = (-G*Mass_Earth*Mp_y)/((Mp_x**2 + Mp_y**2)**1.5)

            Mv_x = Mv_x + Ma_x*delta_time
            Mv_y = Mv_y + Ma_y*delta_time

            Mp_x = Mp_x + delta_time*Mv_x
            Mp_y = Mp_y + delta_time*Mv_y

            Mxs.append(25*Mp_x+Ep_x)        #add x/y positions to the list of moon positions
            Mys.append(25*Mp_y+Ep_y)        #Add the earth positions as well, so it is orbiting around earth. *25 to make the orbit visible

        plt.title(str(delta_time*len(Mxs)/86400)[:4] + " Days")         #title of graph that displays days elapsed
        
        ax.set_xlim(-2.2e11, 2.2e11)        #set the axes as equal
        ax.set_ylim(-2.2e11, 2.2e11)

        ax.plot(Mxs[1:], Mys[1:])           #Plot the moon's coordinates (but not the first one, which ruins the graph)
        ax.plot(Exs, Eys)                   #plot the earth's coordinates
        ax.scatter(0, 0, c="lightblue")     #plot a point to represent the sun
        ax.scatter(Mxs[-1], Mys[-1])        #have a scatter point that represents the moon's current position
        ax.scatter(Exs[-1], Eys[-1])        #have a scatter point that represents the earth's current position

    ani = animation.FuncAnimation(fig, animate, frames=360, interval=20)    #some fancy part of the animation function
    
    plt.axis("equal")                       #equal the axes
    plt.show()                              #show the plot

def static():               #static image of an orbit

    fig1, ax1 = plt.subplots()

    number_of_sectors = 5   #How many ellipse sectors do you want to plot
    max_vertices = 20       #How many differently vertexed polygons do you want to plot
    period_of_sectors = 16  #How far apart do you want the sectors to be

    for a in range(number_of_sectors):  #Runs once for each sector you are plotting
        
        arealist = []       #the list of the different areas for each n-sided polygon
        verticeslist = []   #The list of how many vertices each polygon has
        
        for z in range(max_vertices):   #Runs once for every differently-vertexed polygon

            #Earth around Sun Initials FOR STATIC
            '''G = 6.67e-11
            Mass_Host = 1.9891e30
            p_x = 1.5e11
            p_y = 0
            v_x = 0
            v_y = 29784
            time = 360
            delta_time = 100
            time_increments = time*864'''

            #Mercury around Sun Initials FOR STATIC
            G = 6.67e-11
            Mass_Host = 1.9891e30   #kg
            p_x = 69.82e9           #meters
            p_y = 0
            v_x = 0
            v_y = 38860             #m/s
            time = 88
            delta_time = 100
            time_increments = time*864

            vertices = z        #the number of vertexes the polygon has change. It will iterate through every number from 1 to max_vertices

            firstpoint = 00 + period_of_sectors*a      #MUST be less than/equal to time          #the first point for a time interval
            secondpoint = 10 + period_of_sectors*a     #MUST be less than/equal to time          #the second point of a time interval

            xs = [p_x]            #create a list for x coordinates
            ys = [p_y]            #create a list for y coordinates

            for i in tqdm(range(time_increments)):        #tqdm()       #equations for calculating x and y coords

                a_x = (-G*Mass_Host*p_x)/((p_x**2 + p_y**2)**1.5)       #acceleration calculations
                a_y = (-G*Mass_Host*p_y)/((p_x**2 + p_y**2)**1.5)

                v_x = v_x + a_x*delta_time                              #velocity calculations
                v_y = v_y + a_y*delta_time

                p_x = p_x + delta_time*v_x                              #position calculations
                p_y = p_y + delta_time*v_y

                xs.append(p_x)                                          #add the most recent position to its respective list
                ys.append(p_y)    
            
            if firstpoint != 0:     #makes sure that the code won't break when one interval ending is 0 days
                x1 = xs[round(time_increments/(time/firstpoint))]       #x1 is the first x point on the 2nd law interval
                y1 = ys[round(time_increments/(time/firstpoint))]       #y1 is the first y point on the 2nd law interval
            else:
                x1 = xs[0]
                y1 = ys[0]
            
            if secondpoint != 0:    #makes sure that the code won't break when one interval ending is 0 days
                x2 = xs[round(time_increments/(time/secondpoint))]     #x2 is the last x point on the 2nd law interval
                y2 = ys[round(time_increments/(time/secondpoint))]     #y2 is the last y point on the 2nd law interval
            else:
                x2 = xs[0]
                y2 = ys[0]

            pxs = []                #creates an empty list of the x coords for the infintie polygon
            pys = []                #creates an empty list of the y coords for the infintie polygon

            for i in range(vertices):           #Finds he appropriate points for the polygon's vertices
                pxs.append(xs[round(time_increments/(time/((((abs(firstpoint-secondpoint))/vertices)*(i+1))+min(firstpoint,secondpoint))))])  #find the vertex x location
                pys.append(ys[round(time_increments/(time/((((abs(firstpoint-secondpoint))/vertices)*(i+1))+min(firstpoint,secondpoint))))])  #find the vertex y location
            
            coord = [[x1,y1]]                                           #graphing the infinite polygon
            for i in range(vertices):
                coord.append([pxs[i],pys[i]])
            coord.append([x2,y2])

            coord.append(coord[0]) #repeat the first point to create a 'closed loop'
            polyxxs, polyyys = zip(*coord) #create lists of x and y values
            ax.plot(polyxxs,polyyys, color="green")            

            trianglecoord = [[x1, y1], [x2, y2], [0, 0]]    #graphing the large triangle anchored on the focus
            trianglecoord.append(trianglecoord[0]) #repeat the first point to create a 'closed loop'
            polyxs, polyys = zip(*trianglecoord)   #create lists of x and y values
            
            if a == 0:             #Makes the different polygons different colors. Could be written in one line, but it wouldn't be color coded
                ax.plot(polyxs,polyys,color="red")
            elif a == 1:
                ax.plot(polyxs,polyys,color="orange")
            elif a == 2:
                ax.plot(polyxs,polyys,color="green")
            elif a == 3:
                ax.plot(polyxs,polyys,color="purple")
            else:
                ax.plot(polyxs,polyys, color="lightblue")

            area = shoelace_formula(coord) + shoelace_formula(trianglecoord)        #the area of the total sector (triangle + polygon)
            print("Area of sector: " + str(area))      #calculating and printing the sector area

            arealist.append(area)                      #append arealist with the newfound area
            verticeslist.append(vertices)              #append verticeslist with the correlating number of vertices

            if a == 0:                                 #Plots the relationship between vertices and area, but it is very long bc its color coded
                ax1.plot(verticeslist[1:], arealist[1:], color="red")
                ax1.scatter(verticeslist[1:], arealist[1:], color="red")
            elif a == 1:
                ax1.plot(verticeslist[1:], arealist[1:], color="orange")
                ax1.scatter(verticeslist[1:], arealist[1:], color="orange")
            elif a == 2:
                ax1.plot(verticeslist[1:], arealist[1:], color="green")
                ax1.scatter(verticeslist[1:], arealist[1:], color="green")
            elif a == 3:
                ax1.plot(verticeslist[1:], arealist[1:], color="purple")
                ax1.scatter(verticeslist[1:], arealist[1:], color="purple")
            else:
                ax1.plot(verticeslist[1:], arealist[1:], color="lightblue")
                ax1.scatter(verticeslist[1:], arealist[1:], color="lightblue")
    
    otherfocusx = (2*(max(xs) + min(xs))/2)            #Finds the other focus that is not the Sun

    ax.scatter(otherfocusx,0)                          #Plots that other focus

    '''distances = []                                  #Plots the relationship between point on the ellipse and sum of distance to foci (Ellipse Theory)
    location = []
    for i in range(len(xs)):
        distance1 = math.sqrt((xs[i]**2)+(ys[i]**2))
        distance2 = math.sqrt(((xs[i]-otherfocusx)**2)+(ys[i]**2))        #Must be distance to other focus
        distances.append((distance1+distance2))
        location.append(i)

    ax2.plot(distances)                                #Plot that dude
    plt.ylim(1.1e11,1.2e11)'''                         #set the axis scale so you can see

    plt.title(str(delta_time*len(xs)/86400)[:4] + " Days")      #title in days elapsed

    ax.scatter(x1,y1)                      #graph a point that represents the first day of the 2nd law interval
    ax.scatter(x2,y2)                      #graph a point that represents the second day of the 2nd law interval

    ax.plot(xs, ys)                        #plot the planet's orbit
    ax.scatter(0, 0, c="orange")           #plot a point to represent the sun
    #ax.scatter(xs[-1], ys[-1])            #plot a point to represent that current location of planet
    
    plt.show()                             #Show the plots

static()           #hide which program you do not want, and run which one you do
#live()