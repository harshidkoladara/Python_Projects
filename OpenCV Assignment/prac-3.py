import numpy as np

def compute_rotation_matrix(points, theta):
    theta = np.radians(theta)
    
    centroid = np.mean(points, axis=0)

    translated_points = points - centroid

    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                 [np.sin(theta), np.cos(theta), 0],
                                 [0, 0, 1]], dtype=np.float64)

    rotation_matrix[0:2, 2] = centroid - np.dot(rotation_matrix[0:2, 0:2], centroid)

    return rotation_matrix

points = np.array([[1, 1], [2, 1], [1, 2]])  
theta = 45.0  
rotation_matrix = compute_rotation_matrix(points, theta)
print(rotation_matrix)
