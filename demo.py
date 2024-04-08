'''
Author: Walker Laitala
Date Created: 3/16/24
Last Updated: 4/8/24

Description: A variety of methods for approximating the area underneath your favorite function. Include: Left, Right, & Trapezoid Riemann Sums; Simpon's Rule
Bugs: Color coding only works for the first 8 sections of Simpon's Rule
'''

from Poly import polynomial
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

Poly1 = polynomial([1, 0, 0, 0])

number_of_sections = 8
intervalstart = -10
intervalend = 10

areas = []
xs = []
ys = []

def leftsum():
    for i in range(number_of_sections+1):
        x = (((intervalend - intervalstart)/number_of_sections)*i)+intervalstart
        y = Poly1.plugin(x)

        xs.append(x)
        ys.append(y)

    for i in range(number_of_sections):
        coordxs = []                                           #graphing the square
        coordys = []

        coordxs.append(xs[i])
        coordxs.append(xs[i])
        coordxs.append(xs[i+1])
        coordxs.append(xs[i+1])
        coordxs.append(coordxs[0]) #repeat the first point to create a 'closed loop'
        
        coordys.append(0)
        coordys.append(ys[i])
        coordys.append(ys[i])
        coordys.append(0)
        coordys.append(coordys[0]) #repeat the first point to create a 'closed loop'

        ax.plot(coordxs,coordys)
        
        areas.append(((intervalend - intervalstart)/number_of_sections)*ys[i])

    print("Area: " + str(sum(areas)))

def rightsum():
    for i in range(number_of_sections+1):
        x = (((intervalend - intervalstart)/number_of_sections)*i)+intervalstart
        y = Poly1.plugin(x)

        xs.append(x)
        ys.append(y)

    for i in range(number_of_sections):
        coordxs = []                                           #graphing the square
        coordys = []

        coordxs.append(xs[i])
        coordxs.append(xs[i])
        coordxs.append(xs[i+1])
        coordxs.append(xs[i+1])
        coordxs.append(coordxs[0]) #repeat the first point to create a 'closed loop'

        coordys.append(ys[i+1])
        coordys.append(0)
        coordys.append(0.0)
        coordys.append(ys[i+1])
        coordys.append(coordys[0]) #repeat the first point to create a 'closed loop

        ax.plot(coordxs,coordys)

        areas.append(((intervalend - intervalstart)/number_of_sections)*ys[i+1])

    print("Area: " + str(sum(areas)))

def midpointsum():

    ys = [Poly1.plugin(0)]

    for i in range(number_of_sections+1):
        
        x = (((intervalend - intervalstart)/number_of_sections)*i)+intervalstart
        xs.append(x)

    for i in range(len(xs)-1):

        y = Poly1.plugin((xs[i]+xs[i+1])/2)
        ys.append(y)

    ys.append(Poly1.plugin(xs[-1]))
    
    for i in range(number_of_sections):
        coordxs = []                                           #graphing the square
        coordys = []

        coordxs.append(xs[i])
        coordxs.append(xs[i])
        coordxs.append(xs[i+1])
        coordxs.append(xs[i+1])
        coordxs.append(coordxs[0]) #repeat the first point to create a 'closed loop'

        coordys.append(ys[i+1])
        coordys.append(0)
        coordys.append(0.0)
        coordys.append(ys[i+1])
        coordys.append(coordys[0]) #repeat the first point to create a 'closed loop

        ax.plot(coordxs,coordys)

        areas.append(((intervalend - intervalstart)/number_of_sections)*ys[i+1])

    print("Area: " + str(sum(areas)))

def trapezoidsum():

    ys = [Poly1.plugin(0)]

    for i in range(number_of_sections+1):
        
        x = (((intervalend - intervalstart)/number_of_sections)*i)+intervalstart
        xs.append(x)

    for i in range(len(xs)-1):

        y = Poly1.plugin(xs[i])
        ys.append(y)

    ys.append(Poly1.plugin(xs[-1]))
    
    for i in range(number_of_sections):
        coordxs = []                                           #graphing the trapezoid
        coordys = []

        coordxs.append(xs[i])
        coordxs.append(xs[i])
        coordxs.append(xs[i+1])
        coordxs.append(xs[i+1])
        coordxs.append(coordxs[0]) #repeat the first point to create a 'closed loop'

        coordys.append(ys[i+1])
        coordys.append(0)
        coordys.append(0.0)
        coordys.append(ys[i+2])
        coordys.append(coordys[0]) #repeat the first point to create a 'closed loop

        ax.plot(coordxs,coordys)

        areas.append(((intervalend - intervalstart)/number_of_sections)*((ys[i+1]+ys[i+2])/2))

    print("Area: " + str(sum(areas)))

def simpsons():

    width = (intervalend - intervalstart)/number_of_sections

    if (number_of_sections%2) != 0:
        print("Simpson's Rule only works with an even number of sections, please try again")
        quit()

    sections = []

    for i in range(number_of_sections+1):
        sections.append((width*i)+intervalstart)
    print(sections)
    for i in range(len(sections)):
        if sections[i]%2 == 1:
            sections[i] = 4*sections[i]
        else:
            sections[i] = 2*sections[i]
    
    sections[0] = sections[0]/2
    sections[-1] = sections[-1]/2

    area = (width/3)*sum(sections)

    print("Area: " + str(area))

    ys = [Poly1.plugin(0)]

    for i in range(401):
        
        x = (((intervalend - intervalstart)/400)*i)+intervalstart
        xs.append(x)

    for i in range(len(xs)-1):

        y = Poly1.plugin(xs[i])
        ys.append(y)

    ys.append(Poly1.plugin(xs[-1]))

    for i in range(400):
        coordxs = []                                           #graphing the square
        coordys = []

        coordxs.append(xs[i])
        coordxs.append(xs[i])
        coordxs.append(xs[i+1])
        coordxs.append(xs[i+1])
        coordxs.append(coordxs[0]) #repeat the first point to create a 'closed loop'

        coordys.append(ys[i+1])
        coordys.append(0)
        coordys.append(0.0)
        coordys.append(ys[i+2])
        coordys.append(coordys[0]) #repeat the first point to create a 'closed loop

        if 0<=i<(400/number_of_sections):
            ax.plot(coordxs,coordys, color="lightblue")
        elif (400/number_of_sections)<i<(800/number_of_sections):
            ax.plot(coordxs,coordys, color="yellow")
        elif (800/number_of_sections)<i<(1200/number_of_sections):
            ax.plot(coordxs,coordys, color="lightgreen")
        elif (1200/number_of_sections)<i<(1600/number_of_sections):
            ax.plot(coordxs,coordys, color="orange")
        elif (1600/number_of_sections)<i<(2000/number_of_sections):
            ax.plot(coordxs,coordys, color="purple")
        elif (2000/number_of_sections)<i<(2400/number_of_sections):
            ax.plot(coordxs,coordys, color="green")
        elif (2400/number_of_sections)<i<(2800/number_of_sections):
            ax.plot(coordxs,coordys, color="red")
        elif (2800/number_of_sections)<i:
            ax.plot(coordxs,coordys, color="blue")
        else:
            ax.plot(coordxs, coordys)

simpsons()

Poly1.plot([intervalstart, intervalend+1])         #plot
plt.show()