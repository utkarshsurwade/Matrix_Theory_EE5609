import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


def circ_gen(O, r):
    len = 50
    theta = np.linspace(0, 2 * np.pi, len)  # return evenly spaces nos in interval 50
    x_circ = np.zeros((2, len))  # 2xlen zero matrix
    x_circ[0, :] = r * np.cos(theta)  # r x cos(50 intervals)
    x_circ[1, :] = r * np.sin(theta)  # r x sin(50 intervals)
    x_circ = (x_circ.T + O).T
    return x_circ


# Input parameters
O = np.array(([1, 0]))
P = np.array(([1, 2]))
Q = np.array(([1, -2]))
f = -3
r = np.sqrt(LA.norm(O) ** 2 - f)
m = np.array(([1, 0]))  # direction vector
# k1 = 2
# k2 = -2


##Generating the circle
x_circ = circ_gen(O, r)

# Plotting all lines
x_cor1 = [-1, 3]
y_cor1 = [2, 2]
plt.plot(x_cor1, y_cor1, 'r', label='tangent1')
x_cor2 = [-1, 3]
y_cor2 = [-2, -2]
plt.plot(x_cor2, y_cor2, 'r', label='tangent2')

# Plotting the circle
plt.plot(x_circ[0, :], x_circ[1, :], label='$circle$')

# Labeling the coordinates
tri_coords = np.vstack((P, Q, O)).T
# print(tri_coords)
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['P', 'Q', 'O']
for i, txt in enumerate(vert_labels):  # labeling the points
    plt.annotate(txt,  # this is the text
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')
plt.show()
