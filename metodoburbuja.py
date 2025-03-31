def metodo_burbuja(arr):
    n = len(arr)
    for i in range(n - 1):  
        for j in range(n - 1 - i):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo 
arr = [5, 3, 8, 6, 2]
print(metodo_burbuja(arr)) 
