'''
Author: Walker Laitala
Date Created: 11/29/2023
Date Updated: 1/6/2024

Description: Program that creates a matrix class and lets user run various matrix operations by means of this class
Bugs: Inputs usually must be perfect, so please looks at instructions
'''

class Matrix:                                          #Create matrix class
        '''
        A class that creates a matrix. The various methods apply certain matrix transformations to one or two matrices. They go as follows:

        __init__(): THe initial function that creates a blank (all 0's) matrix if called. It also allows you to call self.columns to find # of columns (same for rows)
        print(): Prints a desired matrix
        plus(): Adds two matrices together, but only if they are of the same dimensions
        times(): Multiplies two matrices together, but only if they are of the proper dimensions
        scalarTimesRow(): Multiplies a desired scalar by a desired row of a matrix
        switchRows(): Switches two rows of a matrix
        linearCombRows(): Takes a row, multiplies it by a desired scalar, then adds that to a different row
        rowreduce(): Reduces a matrix to reduced row echelon form
        invert(): Inverts a matrix

        All methods return/tranform one matrix
        '''
        def __init__(self, rows, columns):             #Initial             #creation of an all 0's matrix. Arguments from when class is called convert to row, column
            '''
            An initial function that creates a blank matrix of desires dimensions
            
            self: the matrix
            rows: the desired amount of rows for the matrix
            columns: the desired amount of columns for the matrix

            Does not return anything, but may update something
            '''
            self.m1 = [[0 for y in range(columns)] for z in range(rows)]           #m1 is a method. It basically lets you access the matric, or an element if used with coordinates
            self.columns = columns                               #a method that will return the mumber of columns in a matridx
            self.rows = rows                                     #a method that will return the number of rows in a matrix
          
        def print(self):                               #Print function
            '''
            a method that prints a matrix

            self: The matrix that will be printed

            Does not return anything, but will print the matrix to the console            
            '''

            for i in range(self.rows):                 #Goes through every element in a given matrix...
                for j in range(self.columns): 
                    if self.m1[i][j] == -0:            #converts a -0 into a 0 if necessary
                        self.m1[i][j] = 0
                    print(self.m1[i][j], end="\t")     #...and prints that element. This also makes sure it looks like a matrix
                print()                                #another piece of   ^

        def plus(self, other):                         #Addition function
            '''
            Adds two matrices together

            self: The first matrix inputted
            other: The second matrix inputted

            Doesn't explicitly return anything, but updates 'self' to be the sum of self + other            
            '''

            if self.rows == other.rows and self.columns == other.columns:       #making sure the matrices are of the same dimensions
                for i in range(self.rows):             #iterates through rows
                    for j in range(self.columns):      #iterates through columns
                        self.m1[i][j] = int(self.m1[i][j]) + int(other.m1[i][j])        #adds the current element with its counterpart in the other matrix
            else:                                      #if the matrices do not have the same dimensions, they can not be added
                print("these matrices can not be added")
                        
        def times(self, other):                        #Multiplication function
            '''
            a method that multiplies two functions together

            self: the first matrix that was inputted
            other: the second matrix that was inputted

            returns a new matrix, output, that is the product of self*other            
            '''

            if self.columns == other.rows:             #Ensures dimensions of matrices allow for matrix multiplication
                
                output = Matrix(self.rows, other.columns)       #Creates a new empty matrix of appropriate dimensions

                for h in range(self.rows):
                    for i in range(other.columns):      #Iterates through all elements
                        for j in range(self.columns):   #but there is an additional iteration, because the process must repeat multiple times in each column
                            output.m1[h][i] += self.m1[h][j]*other.m1[j][i]     #Uses concept of matric multiplication to do appriopraite math
                            
                return output                           #returns the newly created output matrix

            else:                                       #if the matrices can not be multiplies, then say that
                print("These matrices can not be multiplied due to their dimensions")
                return "no"

        def scalarTimesRow(self, scalar, inputrow):    #Scalar function
            '''
            takes a desired scalar and multiplies it by a desired row

            self: the matrix that will be transformed
            scalar: the constant that will be multiplied into a row
            inputrow: the row number of the row that will be transformed

            does not explicitly return anything, but will update 'self' to be equal to scalar*desired_row            
            '''

            for i in range(self.rows):
                for j in range(self.columns):          #iterates through all elements 
                    if i == inputrow:                  #if the current element is in the desired row...
                        self.m1[i][j] = (self.m1[i][j])*scalar  #multiply that element by the desired scalar
                    
        def switchRows(self, row1, row2):              #Row Switching function
            '''
            a method that will switch two rows of a matrix

            self: the matrix that will be transformed
            row1: the first row that will get switched
            row2L the second row that will get switched

            does not explicitly return anything, but will update 'self' to be the same thing but with the two desired rows switched
            '''
            
            original1 = self.m1[int(row1)]             #create a copy of the first row

            self.m1[int(row1)] = self.m1[int(row2)]    #the firstly inputted row of alice turns into the secondly inputted row
            self.m1[int(row2)] = original1             #the secondly inputted row gets turned into the firstly inputted row

        def linearCombRows(self, multiplier, row2, row1):   #Multiplying scalar times row, then adding that to a different row function
            '''
            a method that multiplies a desired scalar times a desired row, then adds that product to a different row. Note: The row that is multiplied by the scalar remains the same

            self: the matrix that will be transformed
            multiplier: the scalar that will be multiplied by row2
            row2: the row that gets multiplied by the scalar and will eventually be added to row1
            row1: the row that becomes the sum of itself + row2*multiplier

            does not explicitly return anything, but will update 'self' with the appropriate transformations
            '''
            for c in range(self.columns):              #for all the columns in the matrix...
                self.m1[row1][c] += multiplier*self.m1[row2][c]     #that element in the desired row += the scalar times that element of the other row

        def rowreduce(self):                           #RREF function
            '''
            reduces a matrix to reduced row echelon form

            self: that matrix that will be RREFed

            returns self, but self has been updated to RREF            
            '''

            for r in range(self.rows):                 #verifies that the diagonal term is not zero. If it is, then switch it with something that isn't
                    if self.m1[r][r] == 0:
                        if r == 0:
                            self.switchRows(r+1,r)
                        else:
                            self.switchRows(r-1,r)


            for r in range(self.rows):                 #for every row in the matrix
                
                counter = 0                            #start a counter at 0
                
                for c in range(self.columns):          #for every column in the matrix
                        if self.m1[r][c] == 0:         #if that element is zero...
                            counter +=1                #add 1 to the counter

                if counter == self.columns:            #if the counter == the number of columns... (this means the entire row is 0's)
                    self.switchRows(r,self.rows-1)     #switch that row with the row below it. Eventually it will end up on the bottom (where we want it)

                variable = self.m1[r][r]               #set variable as the diagonal term
                if variable != 0:                      #Make sure that variable does not = 0 (it shouldn't after the stuff above, but just in case)
                    self.scalarTimesRow(1/variable, r) #divide the whole row by the diagonal term to make to make the diagonal term 1
                    for i in range(r + 1, self.rows):  #Sets everything below the diagonal to 0
                        self.linearCombRows(-self.m1[i][r], r, i)

            for i in range(self.rows):                 #for every row in the matrix
                    for r in range(self.rows):         #go through all the rows again
                        if i != r:                     #Set everything above the diagonal 1's to 0's
                            self.linearCombRows(-self.m1[r][i], i, r)

            
            for r in range(self.rows):                 #for all rows in the matrix          #Will find a 0 0 0 1 contradiction
                counter = 0                            #set a new countr as 0
                for c in range(self.columns):          #for all columns in the matrix
                    if self.m1[r][c] == 0 and self.m1[r][self.columns-1] != 0 and self.rows + 1 == self.columns:    #if the element equals 0, the last element of the row does not equal 0, and #rows + 1 = #cols...
                        counter += 1                   #add 1 to the counter
                if counter == self.columns-1:          #if the counter equals #cols - 1, this means that there is a row of all 0's that somehow equals a nonzero number. That is a contradiction
                    print("\nThere is a contradiction in your matrix. I, the algorithm, am only telling you this \nbecause I, the algorithm, am better than your calculator.\nNonetheless, here is what your mediocre calculator might give you:")
            

            return self                                #return the updated matrix

        def invert(self):                              #Invert function
            '''
            a method that inverts a matrix, if it is of the proper dimensions

            self: the matrix that will be inverted

            returns output, which is the inverted form of self
            '''

            if self.rows != self.columns:              #if the matric is not square...
                print("This matrix is not square, try again")       #tell them that they can't invert it
                main()                                 #send 'em back to start
            processmatrix = Matrix(self.rows, 2*self.columns)   #otherwise, create a new matrix that has twice the columns to work with

            for r in range(self.rows):                 #Set the first half of processmatrix equal to self
                for c in range(self.rows):
                    processmatrix.m1[r][c] = self.m1[r][c]

            for r in range(self.rows):                 #Makes the other half of processmatrix and identity matrix
                processmatrix.m1[r][r+self.rows] = 1   #it is previously all zeroes, so just make the diagonal terms 1

            processmatrix.rowreduce()                  #RREF processmatrix

            
            output = Matrix(self.rows, self.rows)      #make a new matrix of the original dimensions

            for r in range(output.rows):
                for c in range(output.columns):
                    output.m1[r][c] = processmatrix.m1[r][c+self.rows]      #this new output matrix is equal to the second half of process matrix

            return output                              #output is now the properly inverted self matrix, so return output

