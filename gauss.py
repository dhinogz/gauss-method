import numpy as np

"""
A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])

A = np.array([[5, -1, 2], [3, 8, -2], [1, 1, 4]])
b = np.array([-1, 2, 3])
"""

# Sistema de ecuaciones A, b y x
A = np.array([[5, -1, 2], [3, 8, -2], [1, 1, 4]])
b = np.array([-1, 2, 3])
x = np.zeros_like(b)

# Factorizacion LU
L = np.tril(A)
U = A - L

# Inversa de matriz L
L_inv = np.linalg.inv(L)

# x^(k+1) = L^(-1) ⋅ (b - Ux^(k))
# x^(k+1) = (L^(-1) ⋅ b) - (L^(-1) ⋅ Ux^(k)) 
n = 10
for i in range(n):
    x = np.dot(L_inv, b - np.dot(U, x))
    print(x)


