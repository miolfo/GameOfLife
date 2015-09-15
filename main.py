__author__ = 'Forge'
from GameOfLife import game

conway = game.GameOfLife(10, 10)
# conway.start_random_game(5)
arr_of_points = []
# Blinker
# arr_of_points.append(game.Point(2, 1))
# arr_of_points.append(game.Point(2, 2))
# arr_of_points.append(game.Point(2, 3))
# Toad
arr_of_points.append(game.Point(5, 4))
arr_of_points.append(game.Point(6, 4))
arr_of_points.append(game.Point(7, 4))
arr_of_points.append(game.Point(4, 5))
arr_of_points.append(game.Point(5, 5))
arr_of_points.append(game.Point(6, 5))

conway.start_game(arr_of_points)
