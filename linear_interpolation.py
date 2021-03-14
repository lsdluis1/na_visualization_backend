import numpy as np
from numpy_tools import get_func_index, get_x_level, sort_2d_array


def linear_interpolation(points, path_points_num=1000):
    if len(points) <= 1:
        return points
    points = sort_2d_array(np.array(points))
    points_x = points[:, 0]
    points_y = points[:, 1]

    x_arr = np.linspace(points_x[0], points_x[-1], path_points_num)

    func_index = get_func_index(x_arr, points_x)

    return np.array([x_arr, (points_y[func_index + 1] - points_y[func_index]) /
                     (points_x[func_index + 1] - points_x[func_index]) *
                     (x_arr - points_x[func_index]) + points_y[func_index]]).T
