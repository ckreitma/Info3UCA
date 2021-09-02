import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Función particular para escalar de forma manual.
# Sin utilizar la técnica de la multiplicación de matrices.


def escalar(punto, factorx, factory):
    return [punto[0]*factorx, punto[1]*factory]


p1 = [1, 1]
p2 = [8, 2]
p3 = [3, 3]
p4 = [1, 1]
triangulo1 = np.array([p1, p2, p3, p4])

factorx = 1.3
factory = 0.2

triangulo2 = np.array([escalar(p1, factorx, factory), escalar(p2, factorx, factory), escalar(p3, factorx, factory), escalar(p4, factorx, factory)])

plt.figure()

plt.plot(triangulo1[:, 0], triangulo1[:, 1], 'bo-')
plt.plot(triangulo2[:, 0], triangulo2[:, 1], 'ro-')
plt.grid()
plt.show()
