'''
Author: Walker Laitala
Created: 1/7/24
Updated: 1/7/24

Description: A program that allows the user to test out all methods of the Matrix class from WalkerMatrix
Bugs: Inputs usually must be perfect, so please looks at instructions
'''

from WalkerMatrix import Matrix            #Impor the matrix class so everything works

def main():                                #where the UI stuff and all the printing is run out of
    '''
    Allows the user to see each method in action

    takes: none

    returns: none, but will always print something to the terminal
    '''

    alice = Matrix(3,3)                    #MAKE SURE TO UPDATE THESE DIMENSIONS

    alice.m1 = [                           #If you choose to "use the matrices from main," it will run these two matrices. You may edit them as you see fit
        [1, 2, 3], 
        [4, 2, 6],
        [7, 4, 10],
    ]

    trixie = Matrix(4,3)                   #MAKE SURE TO UPDATE THESE DIMENSIONS

    trixie.m1 = [                          #If you choose to "use the matrices from main," it will run these two matrices. You may edit them as you see fit
        [1, 1, 1], 
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    selection = input("Options: \n1 - Print Matrix \n2 - Add Matrices \n3 - Multiply Matrices \n4 - Multiply by Scalar \n5 - Switch Rows \n6 - Linear Combine Rows \n7 - Row Reduce \n8 - Invert Matrix\nWhat would you like to do? (type number)")
    if selection.isnumeric() is not True:  #verifies that selection is an integer
        print("that is not a valid answer")
        main()
    if int(selection) not in [1,2,3,4,5,6,7,8]: #verifies that selection is an option on the menu
        print("that is not a valid answer")
        main()
    matrixanswer = input("If you would like to use the matrices from main (which you may edit as you see fit, but make sure to also update proper dimensions), enter 1.\nIf you would like to see a demonstration of preset example matrices, press 2 ")
    if  matrixanswer != "1" and matrixanswer != "2":    #verifies that answer is legit
        print("that is not a valid answer")
        main()
    else:
        matrixanswer = int(matrixanswer)                #if it is legit, turn it into an integer

    if selection == "1":                   #PRINT - sekection for print function. This simply prints both alice and trixie
        if matrixanswer == 1:              #if the user wants to use their own matrices
            print("alice:")                
            alice.print()                  #prints alice
            print("trixie:")
            trixie.print()                 #prints trixie
        elif matrixanswer == 2:            #if the user wants to use example matrices

            alice = Matrix(3,3)            #create a 3x3 matrix
            alice.m1 = [                   #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]

            trixie = Matrix(3,3)           #create a 3x3 matrix
            trixie.m1 = [                  #Sets the individual elements of alice using a list of lists
                [1, 3, 5], 
                [7, 9, 11],
                [13, 15, 17],
            ]
            print("alice:")
            alice.print()                  #print alice
            print("trixie:")
            trixie.print()                 #print trixie
    
    elif selection == "2":                 #ADD - selection for addition function

        if matrixanswer == 1:              #if the user wants to use their own matrices
            print("alice:")
            alice.print()                  #prints alice
            print("trixie:")
            trixie.print()                 #prints trixie
            print("Alice + Trixie = ")
            alice.plus(trixie)             #Take the object alice and applies the method plus(). The argument is trixie, so trixie gets added to alice. Rewrites alice to be the output matrix of addition function

            alice.print()                  #Runs print method for object alice
        
        elif matrixanswer == 2:

            alice = Matrix(3,3)            #creates a 3x3 matrix
            alice.m1 = [                   #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]

            trixie = Matrix(3,3)
            trixie.m1 = [                  #Sets the individual elements of alice using a list of lists
                [1, 3, 5], 
                [7, 9, 11],
                [13, 15, 17],
            ]
            print("alice:")
            alice.print()                  #prints alice
            print("trixie:")
            trixie.print()                 #prints trixie
            
            print("Alice + Trixie = ")
            alice.plus(trixie)             #alice becomes the sum of alice + trixie
            alice.print()                  #print alice

    elif selection == "3":                 #MULTIPLY - selection for multiplication function

        if matrixanswer == 1:              #if the user wants to use their own matrices
            print("alice:")
            alice.print()                  #prints alice
            print("trixie:")
            trixie.print()                 #prints trixie
            print("Alice * Trixie =")
            alice = alice.times(trixie)    #Take the object alice and applies the method times() with an argument of trixie. This takes alice and multiplies it by trixie
            
            if alice == "no":              #if the matrix is not of the proper dimensions
                pass                       #effectively end it
            else:
                alice.print()                      #print alice

        elif matrixanswer == 2:                    #if the user wants to use example matrices
            alice = Matrix(3,4)                    #creates a 3x4 matrix
            alice.m1 = [                           #Sets the individual elements of alice using a list of lists
                [1, 2, 3, 4],                 
                [4, 5, 6, 7],
                [7, 8, 9, 10],
            ]

            trixie = Matrix(4,3)                   #creates a 4x3 matrix
            trixie.m1 = [                          #Sets the individual elements of alice using a list of lists
                [1, 3, 5], 
                [7, 9, 11],
                [13, 15, 17],
                [1, 2, 3]
            ]
            print("alice:")
            alice.print()                      #prints alice
            print("trixie:")
            trixie.print()                     #prints trixie
            print("Alice * Trixie =")
            alice = alice.times(trixie)        #Take the object alice and applies the method times() with an argument of trixie. This takes alice and multiplies it by trixie
            
            if alice == "no":
                pass
            else:
                alice.print()                  #print alice
  
    elif selection == "4":                     #SCALAR - selection for "scalar multiplied by a row" function

        if matrixanswer == 1:                  #if the user wants to use their own matrices
            print("alice:")
            alice.print()                      #prints alice
            answer = (input("what scalar would you like to multiply by, and to which row? (scalar,row)")).split(",")
            scalar = int(answer[0])            #only works for single digits inputs seperated by comma (i.e.: 4,2)
            inputrow = int(answer[-1])

            print("alice before:")
            alice.print()                               #prints alice
            print("alice, with row " + str(inputrow) + " multiplied by " + str(scalar))
            alice.scalarTimesRow(scalar,inputrow)       #Take object alice and applies method scalarTimesRow() using the inputted scalar, and the desired row. This takes the scalar and multiplies it by the desired row
            alice.print()                      #prints alice
        elif matrixanswer == 2:                #if the user wants to use example matrices
            alice = Matrix(3,3)                #creates a 3x3 matrix
            alice.m1 = [                       #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]
            print("alice before:")
            alice.print()                  #prints alice
            alice.scalarTimesRow(2,0)      #Take object alice and applies method scalarTimesRow() using the inputted scalar, and the desired row. This takes the scalar and multiplies it by the desired row
            print("alice, with row 0 multiplied by 2")
            alice.print()                  #prints alice

    elif selection == "5":                 #SWITCH - selection for switching two rows
        
        if matrixanswer == 1:              #if the user wants to use their own matrices
            print("alice:")
            alice.print()                  #prints alice
            answer = input("What rows of alice would you like to switch? (row,row)")
            row1 = answer[0]                   #Assigns variables to the appriopriate inputs. row1 will be the first row that gets switched
            row2 = answer[-1]                  #row2 will be the second row that gets switched
            print("Here is matrix 'alice' after switching rows " + row1 + " and " + row2)
            alice.switchRows(row1,row2)        #Takes object alice and applies switchRows() to it. This switches row1 of alice with row2 of alice
            alice.print()                      #prints alice

        if matrixanswer == 2:                  #if the user wants to use example matrices
            alice = Matrix(3,3)                #creates a 3x3 matrix
            alice.m1 = [                       #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]
            print("alice before:")
            alice.print()                      #prints alice
            print("Here is matrix 'alice' after switching rows 0 and 2")
            alice.switchRows(0,2)              #Takes object alice and applies switchRows() to it. This switches row1 of alice with row2 of alice
            alice.print()                      #prints alice
            
    elif selection == "6":                     #LINEAR COMBINE - selection for linearCombRows function

        if matrixanswer == 1:                  #if the user wants to use their own matrices
            answer = input("Input row multiplier, which row is being multiplied, and which row the product is being added to | (x,y,z)")
            multiplier = int(answer[0])        #vv sets variables to appropriate inputs. Multiplier will be the multiplier
            row1 = int(answer[2])              #row1 will be the row that gets multiplied by multiplier. This row will not be edited
            row2 = int(answer[-1])             #row2 will be the row that the above product will be added to. 
            print("alice before:")
            alice.print()                      #prints alice
            print("Alice after row " + str(row1) + " is multiplied by " + str(multiplier) + " and added to row " + str(row2) + ":")
            alice.linearCombRows(multiplier, row1, row2)    #takes object alice and appleis method linearCombRows. Takes row1 of alice, multiplies it by multiplier, and adds that product to row2
            alice.print()                      #prints alice
        elif matrixanswer == 2:                #if the user wants to use example matrices
            alice = Matrix(3,3)                #creates a 3x3 matrix
            alice.m1 = [                       #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]
            print("alice before:")
            alice.print()                      #prints alice
            print("Alice after row 0 is multiplied by 2 and added to row 1:")
            alice.linearCombRows(2, 0, 1)      #takes object alice and appleis method linearCombRows. Takes row1 of alice, multiplies it by multiplier, and adds that product to row2
            alice.print()                      #prints alice
    
    elif selection == "7":                     #ROW REDUCE - RREFs a given matrix
        
        if matrixanswer == 1:                  #if the user wants to use their own matrices
            print("alice before:")
            alice.print()                      #prints alice
            alice = alice.rowreduce()          #sets alice as the RREFed version of alice
            print("alice in RREF")
            alice.print()                      #prints alice
        elif matrixanswer == 2:                #if the user wants to use example matrices
            alice = Matrix(3,4)                #creates a 3x4 matrix
            alice.m1 = [                       #Sets the individual elements of alice using a list of lists
                [1, 2, 3, 4], 
                [4, 5, 6, 4],
                [7, 8, 9, 4],
            ]
            print("alice before:")
            alice.print()                       #prints alice
            alice = alice.rowreduce()           #sets alice as the RREFed version of alice
            print("alice in RREF")
            alice.print()                       #prints alice

    elif selection == "8":                      #INVERT - inverts a given matrix      
        
        if matrixanswer == 1:                   #if the user wants to use their own matrices
            print("alice before:")
            alice.print()                       #prints alice
            print("alice, inverted:")
            alice = alice.invert()              #sets alice as the inverted version of alice
            alice.print()                       #prints alice
        elif matrixanswer == 2:                 #if the user wants to use example matrices
            alice = Matrix(3,3)                 #creates a 3x3 matrix
            alice.m1 = [                        #Sets the individual elements of alice using a list of lists
                [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
            ]
            print("alice before:")
            alice.print()                       #prints alice
            print("alice, inverted:")
            alice = alice.invert()              #sets alice as the inverted version of alice
            alice.print()                       #prints alice
    
    else:                                       #If the user has entered something that is not an integer between 1 and 8
        print("You have entered an invalid input. Try again")
        main()                                  #Start over
    
main()                                          #run main and start everything off