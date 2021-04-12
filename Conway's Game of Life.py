import cell
import os
from Grid import grid
from Input_Gui import InputGUI
from tkinter import Button, Tk, Grid, Label, Frame, ttk
from utiliity_functions import clear_screen as cls
from time import sleep
import exceptions

"""Richard Frost"""
"""Main gameplay for project"""

os.system('mode con: cols=100 lines=40')
print("Welcome to Conway's Game of Life")
print("In this game you will fill in spaces on a grid. The game will then progress using the folowing rules")
print("   1. A filled in cell is considered 'living' and an unfilled cell is considered 'dead'")
print("   2. A cell's neighbors are the 8 cells around it")
print("   3. A living cell with less than 2 living neighbors dies")
print("   4. A living cell with exactly 2 or 3 living neighbors remains alive")
print("   5. A living cell with 4 or more living neighbors dies")
print("   6. A dead cell with exactly 3 living neighbors becomes alive\n\n")

while True:
    
    Dimension_String = input("Please enter the dimension of the grid you would like to use. The grid will be a square.\nPlease use a dimension between 3 and 30 (inclusive). Or enter q to quit: ")
    
    if Dimension_String.lower() == 'q':
        break
    
    try:
        Dimension = int(Dimension_String)
    except ValueError:
        cls()
        print("Please enter an integer not a string.\nPlease restart the program and try again.")
        sleep(3)
        break
        
    try:

        if Dimension < 3 or Dimension > 30 and Dimension !=36:
            raise exceptions.DimensionRangeError()

        cls()
        our_grid = grid(Dimension)
        window = Tk()
        input_ui = InputGUI(window, Dimension) #initializes Input gui with gid size Dimension

        window.mainloop()
        selected_cells = input_ui.selected



        for row in range(Dimension): #takes the buttons selected in the ui and fills in those cells on the console
            for col in range(Dimension):
                if selected_cells[row][col] == 1:
                    our_grid.grid[row][col].activate_cell()


        print(our_grid.show_grid())
        input("Please close the other window and make the console full screen. The game will run for 500 generations. Press any key to continue:")

        k = 1
        while k<501: #runs the game for 500 generations
            print(our_grid.advance_grid())
            sleep(.5)
            k +=1

    except exceptions.DimensionRangeError:
        cls()
        print(f'The dimension {Dimension} is not in the specified range. Please Restart the program and try again')
        sleep(3)
        break