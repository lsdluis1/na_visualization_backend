import numpy as np
from linear_interpolation import linear_interpolation
from numpy_tools import get_func_index


def sine_curve(x, start, end, amp):
    sine_y = amp * np.sin(np.pi * (x - start) / (end - start))
    return np.where((x >= start) & (x <= end), sine_y, 0)


def piecewise_sine_curve(x_arr, nodes):
    nodes = np.sort(np.unique(nodes))
    func_index = get_func_index(x_arr, nodes)

    return np.sin(np.pi * (x_arr - nodes[func_index]) /
                          (nodes[func_index + 1] - nodes[func_index]))


def wavy_interpolation(points, amp, clock, path_points_num=100):
    x_arr, linear_y = linear_interpolation(points, path_points_num).T
    points = np.array(points)
    points_x = points[:, 0]

    sine_y = amp * np.sin(clock) * piecewise_sine_curve(x_arr, points_x)

    return np.array([x_arr, sine_y + linear_y]).T
