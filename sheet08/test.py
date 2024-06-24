import numpy as np
import matplotlib.pyplot as plt

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def bubble_sort(arr):
    if is_sorted(arr) == True:
        return arr
    else:
        pos_swap = False
        order = np.identity(len(arr))
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:             
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    temp = order[i].copy()
                    order[i] = order[j]
                    order[j] = temp
                    pos_swap = True
            if pos_swap == False:
                break
        return arr, order


def diagonal_matrix(A):
    tol = 1e-7
    ew = np.linalg.eig(A)[0]
    ew, order = bubble_sort(ew)
    x = np.linalg.eig(A)[1]
    x = x @ order
    U = np.array(x.T)
    D = np.linalg.inv(U) @ A @ U
    for i in range(len(D)):
        for j in range(len(D)):
            if i != j:
                if abs(D[i, j]) < tol:
                    D[i, j] = 0
    print(D)

print(bubble_sort(np.array([5,29,8])))