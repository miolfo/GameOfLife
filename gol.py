__author__ = 'Forge'
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import getopt
from GameOfLife import game

def usage():
    print("")
    print("Usage: ")
    print("Parameters: ")
    print("[-s n] size of the board n*n")
    print("[-r n] randomize board with n live cells")
    print("[-i n] number of iterations per game loop")

def main(argv):
    board_size = 20
    random_cells = 0
    iterations = 0
    try:
        opts, args = getopt.getopt(argv, "s:r:i:")
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s"):
            board_size = int(arg)
        elif opt in ("-r"):
            random_cells = int(arg)
        elif opt in ("-i"):
            iterations = int(arg)

    conway = game.GameOfLife(board_size, board_size)
    if random_cells != 0:
        conway.start_random_game(random_cells, iterations)

if __name__ == "__main__":
    main(sys.argv[1:])