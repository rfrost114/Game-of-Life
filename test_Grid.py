import unittest
from Grid import grid
from Input_Gui import InputGUI

class GridTestCase(unittest.TestCase):
    """Tests for 'Grid.py' and it's interaction with 'cell.py'."""

    def test_activate_cell(self):
        """Tests the activation of a single cell"""

        self.sample_grid = grid(3)
        self.sample_grid.grid[0][0].activate_cell()
        self.assertTrue(self.sample_grid.grid[0][0].check_alive())

    def test_kill_cell(self):
        """Tests the killing of a single cell"""
        self.sample_grid = grid(3)
        self.sample_grid.grid[0][0].activate_cell()
        self.sample_grid.grid[0][0].kill_cell()
        self.assertFalse(self.sample_grid.grid[0][0].check_alive())

    def test_advance_grid(self):
        """Checks that advancement works as expected for a simple set up"""

        self.sample_grid = grid(3)
        self.sample_grid.grid[1][0].activate_cell()
        self.sample_grid.grid[1][1].activate_cell()
        self.sample_grid.grid[1][2].activate_cell()
        self.sample_grid.advance_grid()
        self.assertTrue(self.sample_grid.grid[0][1].check_alive())
        self.assertTrue(self.sample_grid.grid[1][1].check_alive())
        self.assertTrue(self.sample_grid.grid[2][1].check_alive())
        

    def test_default_dimension(self):
        """Checks to see if default grid size is used if an improper data type is passed for dim"""

        self.sample_grid = grid('lamp')
        self.assertEqual(self.sample_grid.dim, 4)

    def test_show_grid(self):
        """Checks to see if the grid prints correctly"""

        self.sample_grid = grid(3)
        self.assertEqual(self.sample_grid.show_grid(), ' | | \n-+-+-\n | | \n-+-+-\n | | ')




if __name__ == '__main__':
    unittest.main()