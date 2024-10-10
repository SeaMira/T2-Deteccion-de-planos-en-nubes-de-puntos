import numpy as np
from tqdm import tqdm
from .utils import get_3_random_points_indexes
from .plane import Plane

def get_plane(cloud, p1, p2, p3, min_points, threshold, i1, i2, i3):
    # print("AA", type(cloud[0]))
    plane = Plane(p1, p2, p3, i1, i2, i3)
    for i in range(len(cloud)):
        dist = plane.dist_from_p(cloud[i])
        if i == i1 or i == i2 or i == i3:
            continue
        if dist < threshold:
            plane.add_inlier(cloud[i])
            plane.add_cloud_indexes(i)
    return plane, plane.is_plane(min_points)



def find_planes(cloud, p, min_points, iterations):
    planes = []
    new_tries_amount = 0.1*min_points
    amount = len(cloud)
    not_consecutive_planes = 0
    print("Amount of points in cloud:", amount)
    for i in tqdm(range(iterations)):
        
        if amount <= min_points:
            break
        i1, i2, i3 = get_3_random_points_indexes(amount-1)
        plane, is_plane = get_plane(cloud, cloud[i1], cloud[i2], cloud[i3], min_points, p, i1, i2, i3)
        if is_plane:
            plane.make_copy()
            planes.append(plane)
            cloud = np.delete(cloud, plane.cloud_indexes, axis=0)
            amount = len(cloud)
            not_consecutive_planes = 0
        else:
            not_consecutive_planes += 1
            if not_consecutive_planes == 10:
                min_points -= new_tries_amount
                not_consecutive_planes = 0
    return planes
