#Ejercicio 1: Suma de los primeros N números
numero_n = int(input("Ingrese la cantidad de N numeros naturales: "))
suma = 0
for num in range (1,numero_n+1):
    suma += num
print ("La suma es de los primeros N naturales es:", suma)

#Ejercicio 2: Factorial de un número
numero = 9
factorial = 1
for i in range (1,numero + 1):
    factorial = factorial * i
print(factorial)

#Ejercicio 3: Tabla de multiplicar
numero = int(input("Ingrese el numero de la Tabla de Multiplicar: "))
for i in range (1,11):
    multi = i * numero
    print(f"El numero: {numero} por: {i} Es: {multi}")

#Ejercicio 4: Cálculo de promedio de notas
suma_notas = 0
contador_notas = int(input("ingrese el numero de notas: "))
for i in range (contador_notas):
    calif = int(input(f"Calificacion numero {i + 1} Ingrese la calificacion: "))
    suma_notas += calif
    promedio = suma_notas / contador_notas
print ("El promedio final es de: ", promedio)

#Ejercicio 5: Potencia de un número
numero_base = int(input("Ingrese el numero a sacar potencia: "))
exponente = int(input("Escriba el exponente para el numero: "))
resultado = 1
for i in range (exponente):
    resultado *= numero_base
print("La potencia es: ", resultado)

#Ejercicio 6: Suma de números pares en un rango
a = 1
b = 20
suma = 0
for i in range (a, b + 1 ):
    if (i % 2 == 0):
        suma += i
print("La suma de los numeros pares es: ", suma)
