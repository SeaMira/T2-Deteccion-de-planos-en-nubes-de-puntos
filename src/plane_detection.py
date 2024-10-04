import numpy as np
from .utils import get_3_random_points_indexes
from .plane import Plane

def get_plane(cloud, p1, p2, p3, min_points, threshold):
    plane = Plane(p1, p2, p3)
    for p in cloud:
        dist = plane.dist_from_p(p)
        if dist < threshold:
            plane.add_inlier(p)
    return plane, plane.is_plane(min_points)



def find_planes(cloud, p, min_points, iterations):
    planes = []
    amount = len(cloud)
    print("Amount of points in cloud:", amount)
    for i in range(iterations):
        i1, i2, i3 = get_3_random_points_indexes(amount-1)
        plane, is_plane = get_plane(cloud, cloud[i1], cloud[i2], cloud[i3], min_points, p)
        if is_plane:
            planes.append(plane)
    return planes
