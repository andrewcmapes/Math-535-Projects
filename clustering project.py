# File for exploring clustering algorithms
import matplotlib.pyplot as plt
import numpy as np

points = np.random.randn(400,2)

def sorter(x: np.ndarray, k_reps: np.ndarray):
    distances = np.linalg.norm(x[:, np.newaxis]-k_reps, axis=2)
    assignments = np.argmin(distances, axis=1)
    return assignments

def kmeans(points: np.ndarray, k: int, iterations: int = 5):
    dim = points[0].shape
    representitives = [points[i] for i in range(k)]
    assignments = sorter(points, representitives)
    for i in range(iterations):
        representitives = np.array([points[assignments == i].mean(axis=0) for i in range(k)])
        assignments = sorter(points, representitives)
        plt.scatter(points[:,0],points[:,1], c=assignments)
        plt.show()
    return assignments, representitives


X, Y = kmeans(points, 4)