#ARREGLO burbuja
#Julia Esther de la Torre Herrera

def bubble_sort(arr):#definimos el arreglo de tipo burbuja
    n = len(arr)
    # Iterar a través de todos los elementos en la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(n-i-1):
            # Intercambiar elementos si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("Organiza tus ingresos de mes")

# Pedir al usuario que introduzca los valores a ordenar
arr = []
n = int(input("Introduce la cantidad ingresos del mes: "))
for i in range(n):
    val = int(input("Introduce el valor {}: ".format(i+1)))
    arr.append(val)

# Llamar a la función bubble_sort para ordenar la lista
sorted_arr = bubble_sort(arr)

# Imprimir la lista ordenada
print("Lista ordenada:")
for i in range(len(sorted_arr)):
    print(sorted_arr[i], end=' ')

print("\nTu mayor ingreso fue de:", sorted_arr[-1])

#Este metodo nos sirve para organizar cualquier tipo de datos y ponerlos en orden cronologico , en la vida diaria podemos organizar cosas hasta de una empresa 
