__author__ = 'Forge'
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from GameOfLife import game
conway = game.GameOfLife(20, 20)
conway.start_random_game(20, 0)
arr_of_points = []
# Blinker
# arr_of_points.append(game.Point(1, 1))
# arr_of_points.append(game.Point(1, 2))
# arr_of_points.append(game.Point(1, 3))
# Toad
# arr_of_points.append(game.Point(5, 4))
# arr_of_points.append(game.Point(6, 4))
# arr_of_points.append(game.Point(7, 4))
# arr_of_points.append(game.Point(4, 5))
# arr_of_points.append(game.Point(5, 5))
# arr_of_points.append(game.Point(6, 5))
# conway.start_game(arr_of_points)
