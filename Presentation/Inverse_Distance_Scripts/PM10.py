from math import sqrt
import matplotlib.pyplot as plt 
from matplotlib import colors 
import numpy as np 
import csv


def mod(x):
    if(x < 0):
        return -1 * x
    else:
        return x


def dist(x1, y1, x2, y2):
    mult = 10
    x = mod(x2-x1) + 1
    y = mod(y2-y1) + 1
    if(x2 == x1):
        return y * mult * y * mult
    elif(y2 == y1):
        return x * mult * x * mult
    else:
        return ((x*x) + (y*y)) * mult * mult


pts = [(5, 4), (5, 21), (1, 40), (17, 40), (30, 40), (37, 42), (23, 25), (28, 4), (15, 11)]

data = np.random.rand(51, 50) * 0
with open('Location values.csv') as file:
    csvData = csv.reader(file, delimiter=',')
    for row in csvData:
        data[int(row[0])][int(row[1])] = float(row[8])

for i in range(51):
    for j in range(50):
        if((i, j) not in pts):
            d = 0;
            for pt in pts:
                d = d + (1/dist(i, j, pt[0], pt[1]))
                data[i][j] = data[i][j] + (1/dist(i, j, pt[0], pt[1]) * data[pt[0]][pt[1]])
            data[i][j] = data[i][j] / d

# create discrete colormap
cmap = colors.ListedColormap(['green', 'yellow', 'orange', 'red', 'purple'])
bounds = [0, 50, 100, 250, 350, 430]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)
# draw gridlines
ax.grid(which='major', axis='both', linestyle=':', color='k', linewidth=0.5)
ax.set_xticks(np.arange(-.5, 50, 1))
ax.set_yticks(np.arange(-.5, 51, 1))

plt.savefig('PM10.png')
