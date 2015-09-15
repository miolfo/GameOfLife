__author__ = 'Forge'
import game

conway = game.GameOfLife(10, 10)
# conway.start_random_game(5)
arr_of_points = []
arr_of_points.append(game.Point(2, 1))
arr_of_points.append(game.Point(2, 2))
arr_of_points.append(game.Point(2, 3))
conway.start_game(arr_of_points)
