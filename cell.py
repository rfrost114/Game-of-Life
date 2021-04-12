class cell:
    """class for a single cell"""

    def __init__(self):
        """A cell is dead by default and has a name cooresponding to its number in the grid"""

        self.status = 'dead'
    
    def kill_cell(self):
        """kills a cell"""
        self.status = 'dead'

    def activate_cell(self):
        """Sets a cell's status to alive"""

        self.status = 'alive'

    def check_alive(self):
        """Checks if a cell is alive or dead"""

        if self.status == 'alive':
            return True
        else:
            return False
    
    def grid_symbol(self):
        """returns a symbol cooresponding to a cell's status""" 

        if self.check_alive():
            return '█'
        else:
            return ' '
