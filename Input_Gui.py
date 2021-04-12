from tkinter import Button, Tk, Grid, Label, Frame, ttk
from functools import partial
from time import sleep
from utiliity_functions import clear_screen as cls

class InputGUI:
    """A class for a gui to allow easy selection of cells by the player"""

    def __init__(self, master, dim):
        """Creates a window with a grid of buttons with dimension dim, instructions, and a submit button"""

        self.master = master #the main window
        master.title("Conway's Game of Life Input") #main window title
        
        try:
            self.dim = int(dim) #grid dimension
        except ValueError:
            cls()
            print("Improper Data type for Dim. Using Default Value of 4")
            sleep(2)
            self.dim = 4

        self.buttons = [['' for x in range(self.dim)] for y in range(self.dim)] #an array to hold buttons
        self.selected = [['' for x in range(self.dim)] for y in range(self.dim)] #an array to hold what buttons are clicked
        info = Label(text='Please enter the spaces you would like to fill') #instructions for the player

        Grid.rowconfigure(self.master, 0, weight=1) #configures button grid rows
        Grid.columnconfigure(self.master, 0, weight=1) #configures button grid columns

        self.frame = Frame(master) #a frame to hold the buttons
        exit_button = Button(self.frame, text="Click When Done", command=self.submit) #a submitt button
        exit_button.grid(row=0, column=self.dim + 1, sticky='nsew') #puts exit button on grid
        info.grid(row=0, column=0) #puts instructions on grid
        self.frame.grid(row=1, column=0, sticky='nsew')

        for row_index in range(self.dim): #makes grid of buttons
            Grid.rowconfigure(self.frame, row_index, weight=1)
            for col_index in range(self.dim):
                Grid.columnconfigure(self.frame, col_index, weight=1)
                self.buttons[row_index][col_index] = Button(self.frame, bg='#ffffff', command=partial(self.when_pressed, row_index, col_index)) # buttons execute 'when_pressed'
                self.buttons[row_index][col_index].grid(row=row_index, column=col_index, sticky='nsew')

    def when_pressed(self, row, col):
        """Fills in values in an array to represent what spaces a player has selected"""

        self.buttons[row][col].configure(bg='yellow') # button becomes yellow when pressed
        self.selected[row][col] = 1 #selected array gets a marker to show that a button was pressed

    def submit(self):
        
        
        self.master.quit()
    

if __name__ == '__main__':
    #testing
    root = Tk()
    lol = InputGUI(root, 5)
    root.mainloop()
