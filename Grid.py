from cell import cell
from utiliity_functions import clear_screen as cls
from time import sleep
import os

class grid(cell):
    """A Class for the grid that cells live in"""

    def __init__(self, dim):
        """A Grid is square with dimension dim, each place in the grid contains a cell"""

        try:
            self.dim = int(dim)
        except ValueError:
            print("Improper Data Type. Using default dimension 4 instead")
            sleep(3)
            cls()
            self.dim = 4
            
        self.grid = [[cell() for x in range(self.dim)] for y in range(self.dim)] #square array of size dim with each element as a cell
        
   
    def show_grid(self):
        """Creates an ASCII representation of the grid and cells in the console"""

        middle_string = '' #a string of +'s and -'s that goes between each row
        output_list = [] #a list 

        for y in range(1, (self.dim *2)): #makes the middle_string be the right size for the given dimension
            if (y%2) == 0:
                middle_string +='+'
            elif (y%2) != 0:
                middle_string +='-'

        for y in self.grid:  #makes a visual representation of a the grid by appending strings to the output_list
            for x in y:
                if (y.index(x) + 1) % len(y) != 0:  #if a cell in a grid row is not the last space in the row
                    output_list.append(f"{x.grid_symbol()}|")
                elif (y.index(x) + 1) % len(y) == 0 and (self.grid.index(y) + 1) != self.dim: #if a cell in a grid row is the last cell in that row and isn't the very last row
                    output_list.append(f"{x.grid_symbol()}\n{middle_string}\n")
                elif (y.index(x) + 1) % len(y) == 0 and (self.grid.index(y) + 1) == self.dim: #if a cell in a grid row is the last cell in that row and is the very last row
                    output_list.append(f"{x.grid_symbol()}")
        
        grid_string = ''.join(map(str, output_list)) #makes output_list into a string and returns it
        return grid_string
    
    def cell_set(self, x, y):
        """Makes a certain cell in the grid alive mostly for testing"""

        col = y
        row = x
        self.grid[row][col].activate_cell()

    def advance_grid(self):
        """advances the game by 1 generation"""

        hit_grid = [['' for x in range(self.dim)] for y in range(self.dim)] #an empty dim x dim array that will hold the number of living neighbors a cells has
        for y in self.grid:
            for x in y:
                hit_list = [] # a list that will hold a one for each living neightbor a cell has
                row_val = self.grid.index(y)
                col_val = y.index(x)

                #the next 8 if statements check to see if the 8 neighbors of a cell are alive, they also take into account the bounds of the grid
                if (row_val - 1) != -1 and self.grid[row_val - 1][col_val].check_alive() == True: 
                    hit_list.append(1)
                
                    
                if (row_val - 1) != -1 and (col_val - 1) != -1 and self.grid[row_val - 1][col_val - 1].check_alive() == True:
                    hit_list.append(1)
                
                    
                if (col_val - 1) != -1 and self.grid[row_val][col_val - 1].check_alive() == True:
                    hit_list.append(1)
                

                if (row_val + 1) <= (self.dim - 1) and (col_val - 1) != -1 and self.grid[row_val + 1][col_val - 1].check_alive() == True:
                    hit_list.append(1)
                

                if (row_val + 1) <= (self.dim - 1) and self.grid[row_val + 1][col_val].check_alive() == True:
                    hit_list.append(1)
               

                if (row_val + 1) <= (self.dim - 1) and (col_val + 1) <= (self.dim - 1) and self.grid[row_val + 1][col_val + 1].check_alive() == True:
                    hit_list.append(1)
                

                if (col_val + 1) <= (self.dim - 1) and self.grid[row_val][col_val + 1].check_alive() == True:
                    hit_list.append(1)
                
                if (row_val - 1) != -1 and (col_val + 1) <= (self.dim - 1) and self.grid[row_val - 1][col_val + 1].check_alive() == True:
                    hit_list.append(1)
                
                hit_grid[row_val][col_val] = len(hit_list) #puts the number of living neighbors of a givin cell into the corresponding place of of that cell on the hitgrid
                
        for i in self.grid: #uses the completed hit_grid to carry out generation advancement
            for j in i:
                new_row_val = self.grid.index(i)
                new_col_val = i.index(j)
                if j.check_alive() == False: #if a dead cell has 3 living neighbors it becomes alive
                    if hit_grid[new_row_val][new_col_val] == 3:
                        j.activate_cell()
                elif j.check_alive() == True:
                    if hit_grid[new_row_val][new_col_val] == 0 or hit_grid[new_row_val][new_col_val] == 1: #if a living cell has 1 or 0 living neighbors it dies
                        j.kill_cell()
                    elif hit_grid[new_row_val][new_col_val] >= 4: #if a living cell has 4 or more living neighbors it dies
                        j.kill_cell()
                    elif hit_grid[new_row_val][new_col_val] == 2 or hit_grid[new_row_val][new_col_val] == 3: #if a living cell has 2 or 3 living neighors it survives
                        pass
        cls() #clears the screen
        return self.show_grid() #returns the new grid




if __name__ == '__main__':
    #testing

    lol = grid(3)
    os.system('mode con: cols=100 lines=40')

    #lol.cell_set(1,2)
    #lol.cell_set(2,2)
    #lol.cell_set(3,1)
    #lol.cell_set(3,2)
    #lol.cell_set(3,3)
    print(lol.show_grid())
    input()
    k = 1
    while k<200:
        print(lol.advance_grid())
        sleep(.5)
        k +=1
    
