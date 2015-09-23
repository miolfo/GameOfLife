__author__ = 'Forge'
import random


class Point:
    """
    A class for containing a point with x and y coordinates
    """

    def __init__(self, y, x):
        self.y = y
        self.x = x


class GameOfLife:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.game_board = self.Board(board_width, board_height)

    def start_random_game(self, no_of_cells, iterations):
        """
        Start a game with live cells in random positions
        :param no_of_cells: Number of cells generated to the board
        :return:
        """
        for i in range(no_of_cells):
            x_coord = random.randint(0, self.board_width - 1)
            y_coord = random.randint(0, self.board_height - 1)
            self.game_board.set_cell_status(Point(x_coord, y_coord), 1)
        self.game_loop(iterations)

    def start_game(self, array_of_points):
        """
        Start a game with predefined live cells
        :param array_of_points: Array containing all points that will be set
        as live
        """
        for point in array_of_points:
            self.game_board.set_cell_status(point, 1)
        self.game_loop()

    def game_loop(self, iterations):
        print("Started a game with following board: ")
        self.game_board.print_board()
        print("------------------------------------")
        if iterations == 0:
            while True:
                self.single_iteration()
                self.game_board.print_board()
                input("Press Enter for next iteration")
        else:
            while True:
                for i in range(0, iterations):
                    self.single_iteration()
                self.game_board.print_board()
                input("Press Enter for next iteration")


    def single_iteration(self):
        """
        Go through all the game of life rules and determine the next
        iteration for the board
        """
        self.apply_rules()

    def apply_rules(self):
        """
        Apply Conway's Game Of Life rules (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
        """
        # Create a copy of the board
        next_iter_live_cells = []
        for i in range(0, self.board_width):
            for j in range(0, self.board_height):
                live_neighbours = self.check_neighbours(Point(i, j))
                this_cell_status = self.game_board.board_values[j][i]
                if (live_neighbours == 2 or live_neighbours == 3) and this_cell_status == 1:
                    next_iter_live_cells.append(Point(i, j))
                if live_neighbours == 3 and this_cell_status == 0:
                    next_iter_live_cells.append(Point(i, j))

        self.game_board = self.Board(self.board_width, self.board_height)
        for point in next_iter_live_cells:
            self.game_board.set_cell_status(point, 1)

    def check_neighbours(self, point):
        """
        Calculate the amount of live neighbours of the point
        :param point: Point whose neighbours should be checked
        :return: number of live cells in neighbours
        """
        live_cells = 0
        for i in range(-1, 2):
            # print(point.x, point.y + i)
            # print(self.game_board.board_values[point.x][point.y + i])
            for j in range(-1, 2):
                if point.x + j < 0 or point.x + j >= self.board_width or point.y + i < 0 or point.y + i >= self.board_height:
                    break

                curr_cell_status = self.game_board.board_values[point.x + j][
                    point.y + i]
                if curr_cell_status == 1:
                    if not (i == 0 and j == 0):
                        live_cells += 1
        return live_cells

    class Board:
        """
        Class for holding the data of a board, generating different boards
        and printing the board
        """

        def __init__(self, board_width, board_height):
            """
            Create a board with specified dimensions
            :param board_width: Width of the board
            :param board_height: Height of the board
            """
            self.__board_width = board_width
            self.__board_height = board_height
            self.board_values = [[0 for x in range(board_width)] for x in
                                 range(board_height)]

        def set_cell_status(self, point, status):
            """
            Set the status of a single cell
            :param point: Point in which the cell is set
            :param status: Status (0 = dead, 1 = alive)
            """
            self.board_values[point.x][point.y] = status

        def print_board(self):
            """
            Print the contents in the board
            """

            for array in self.board_values:
                single_line = "|"
                for value in array:
                    if value == 1:
                        single_line += "X" + "  "
                    else:
                        single_line += "." + "  "
                single_line += "|"
                print(single_line)
