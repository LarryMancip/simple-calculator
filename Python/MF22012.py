def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a / b

print("Bienvenido a la Calculadora")
print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Ingresa el número de la operación (1-4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    print("Resultado:", sumar(num1, num2))
elif opcion == '2':
    print("Resultado:", restar(num1, num2))
elif opcion == '3':
    print("Resultado:", multiplicar(num1, num2))
elif opcion == '4':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opción inválida")