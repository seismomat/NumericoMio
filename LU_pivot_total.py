import numpy as np


def lu_pivot_total(A):
    n = A.shape[0]
    P = np.eye(n)  # Matriz de permutación inicial
    LU = A.copy()
    
    for k in range(n - 1):
        pivot_row = np.argmax(np.abs(LU[k:n, k])) + k
        if pivot_row != k:
            P[[k, pivot_row]] = P[[pivot_row, k]]
            LU[[k, pivot_row]] = LU[[pivot_row, k]]
        
        for i in range(k + 1, n):
            LU[i, k] /= LU[k, k]
            for j in range(k + 1, n):
                LU[i, j] -= LU[i, k] * LU[k, j]

    return P, LU

# Ejemplo de uso
A = np.array([[2, 1, 1],
              [4, 3, 3],
              [8, 7, 9]], dtype=float)

P, LU = lu_pivot_total(A)
print("Matriz de permutación P:")
print(P)
print("Matriz triangular inferior L y superior U:")
print(LU)
