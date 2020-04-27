
print("BIENVENIDO A FIZZBUZZ!! - ESPERO QUE LO PASES BIEN!")

# Pedimos un numero al usuario entre 1 y 100.
num_usuario = int(input("Introduzca un numero entre 1 y 100: "))

# Mediante un while filtramos que no se introduzca un nº fuera del rango permitido.
while num_usuario <= 0 or num_usuario > 100:

    # Mostramos un mensaje de error y se repite el bucle hasta introducir un numero correcto.
    num_usuario = int(input("\nERROR! NUMERO FUERA DE RANGO - Introduzca un numero entre 1 y 100: "))

# Realizamos las comprobaciones HASTA el numero que ha introducido el usuario e imprime por pantalla.
for contador in range(1, num_usuario + 1):

    if contador % 3 == 0 and contador % 5 == 0:
        print("fizzbuzz")

    elif contador % 3 == 0:
        print("fizz")

    elif contador % 5 == 0:
        print("buzz")

    else:
        print(contador)