import numpy as np
from .utils import distancia_punto_a_plano

class Plane:
    def __init__(self, p1, p2, p3, i1, i2, i3):
        self.inliers = [p1, p2, p3]
        self.cloud_indexes = [i1, i2, i3]
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
        # Dos vectores del plano
        v1 = p2 - p1
        v2 = p3 - p1
        
        # Producto cruz para normal del plano
        normal = np.cross(v1, v2)
        
        # Los coeficientes A, B y C son los componentes de la normal
        self.A, self.B, self.C = normal
        
        # Calculamos D usando uno de los puntos (en este caso, p1)
        self.D = -np.dot(normal, p1)

    def dist_from_p(self, p):
        dist = distancia_punto_a_plano(self.A, self.B, self.C, self.D, p)
        return dist

    def add_inlier(self, p):
        self.inliers.append(p)

    def add_cloud_indexes(self, i):
        self.cloud_indexes.append(i)

    def is_plane(self, min_inliers_amount):
        return len(self.inliers) >= min_inliers_amount

    def points(self):
        return np.array(self.inliers)
    
    def make_copy(self):
        for i in range(len(self.inliers)):
            self.inliers[i] = np.copy(self.inliers[i])