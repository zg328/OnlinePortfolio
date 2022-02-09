"""
2/9/2022
this is the basic sudoku solver algorithm that I am using as a base for
the rest of my sudoku solver needs. 
"""
import numpy as np
puzzle = np.zeros((9,9))
#print(puzzle)

"""
the SeePuzzle method is used to allow the user to see the
puzzle in a formated way. I do need to come back and improve
this because just looking at it I know I can make it more
efficiently. 
"""             
def SeePuzzle(puzzle):
    print("-------------------------")
    for i in range(9):
        for j in range(9):
            if j == 3 or j == 6:
                print( " | "+str(int(puzzle[i][j])),end="")
            elif j == 8:
                print(" " + str(int(puzzle[i][j]))+ " |")
            elif j == 0:
                print( "| "+str(int(puzzle[i][j])),end="")
            else:
                print(" " + str(int(puzzle[i][j])),end="") 
        if i == 2 or i == 5:
            print("-------------------------")
    print("-------------------------")
SeePuzzle(puzzle)                      
                    
        
        