import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import random

height = 1500
width = 1500
n = 10
points = np.zeros((n,2))
points[:,0] = np.random.randint(0, width, n)
points[:,1] = np.random.randint(0, height, n)
triangulation = Delaunay(points)
centers = np.sum(points[triangulation.simplices], axis=1, dtype='int')/3.0
colors = np.array([ (x-width/2.)**2 + (y-height/2.)**2 for x,y in centers])
plt.axis('off')
plt.tripcolor(points[:,0], points[:,1], triangulation.simplices.copy(), facecolors=colors, edgecolors='k')
plt.savefig('randomap', dpi = 500)
plt.show()


