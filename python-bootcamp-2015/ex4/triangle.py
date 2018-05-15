import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)

triangle = {'A': (0, 0),
            'B': (4, 0),
            'C': (2, 2)}

def random_points(nsteps = 10000):
    starting = (2, 1)
    corners = np.random.choice(triangle.keys(), nsteps)
    points = np.array([starting])
    points = np.append(points, np.array(triangle.values()), axis=0)
    for i in range(nsteps):
        corner = corners[i]
        newx = (starting[0] + triangle[corner][0]) / 2.0
        newy = (starting[1] + triangle[corner][1]) / 2.0
        new_point = np.array([(newx, newy)])
        starting = (newx, newy)
        points = np.append(points, new_point, axis=0)
    return points

points = random_points()
plt.scatter(points[:, 0], points[:, 1])
plt.savefig('Sierpinski.png')
        
    
    
