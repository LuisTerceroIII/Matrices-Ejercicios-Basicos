#Ejercicios basicos - Matriz

#Ejercicio 1
#funcion que recibe una matriz y un entero e indica si el entero esta en la matriz.
def appears(matrix,integer):
    for list1 in matrix:
        for number in list1:
            if(number == integer):
                return True
    return False
#Ejercicio 2
#Hacer una funcion que dado un entero y una matriz de enteros devuelva una lista de 
# cuantas veces aparece el entero en cada lista.
numbers = [[1,2,5,5,5],[5,8,7],[10,47,5],[6,9,7],[3,6,7]]
def timesItAppears(matrix,number):
    count = 0
    newList = [[],[],[],[],[]]
    for i in range(len(matrix)):#5
        for j in range(len(matrix[i])):#3
            if(number == matrix[i][j]):
                count = count + 1
        newList[i].append(count)
        count = 0
    return newList
#print(timesItAppears(numbers,5))

#Ejercicio 3
#Hacer una funcion que reciba una matriz de enteros y la modifique ubicando
#el maximo de cada fila a la ultima posicion de la fila 
def orderList(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - i):
            if(matrix[i][j] > matrix[i][j + 1]):
                aux = matrix[i][j]
                matrix[i][j] = matrix[i][j+1]
                matrix[i][j+1] = aux

print(orderList(numbers))                

