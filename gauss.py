""" Metodo de Jacobi """

import numpy as np




# Ask for system of equations
def SystemEquations():  
    N = int(input("Cantidad de ecuaciones en el sistema: "))
    sysEq = []  

    for i in range(N):
        print("Ecuacion", i+1)
        sysEq.append([])
        for j in range(N):
            x = int(input("Constante de x" + str(j+1) + ": "))

            sysEq[i].append(x)
            print(sysEq)

    return sysEq

def SystemZero():  
    N = int(input("Cantidad de ecuaciones en el sistema: "))
    sysZero = []  

    for i in range(N):
        print("Ecuacion", i+1)
        sysZero.append([])
        for j in range(N):
            x = 0

            sysZero[i].append(x)

    return sysZero

def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))


def main():
    matrizA = SystemEquations()
    matriz0 = SystemZero()
    n = int(input("Cantidad de iteraciones: "))
    for i in range(n):
        x_n = matriz0
        
        for j in range(len(A)):
            pass

main()

