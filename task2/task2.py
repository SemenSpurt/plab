## Task 2
import sys


def is_point_in_ellipse(
        point: list,
        center: list,
        radius_x: float,
        radius_y: float
    ) -> int:

    x, y = point
    cx, cy = center

    dx = x - cx
    dy = y - cy

    value = (dx * dx) / (radius_x * radius_x) + (dy * dy) / (radius_y * radius_y)
    
    if abs(value - 1.0) <= 1e-9:
        return 0
    elif value < 1.0:
        return 1
    else:
        return 2



if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        [e, r] = f.readlines()
        center = [float(i) for i in e.split()]
        radius_x, radius_y = [float(i) for i in r.split()]

    with open(sys.argv[2]) as f:
        points = [[float(j) for j in i.split()] for i in f.readlines() if i != ""]

    for point in points:
        print(is_point_in_ellipse(point, center, radius_x, radius_y))