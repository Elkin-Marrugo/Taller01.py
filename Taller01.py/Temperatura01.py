# FUNDACION UNIVERSITARIA TECNOLOGICO COMFENALCO
# ACTIVIDAD DE PROGRAMACION
# PROGRAMA: Ingeniería Industrial
# DOCENTE: Ing. Alexander Diaz Chico
# ESTUDIANTE: Elkin Marrugo Elles.
def main():

    # Lista para almacenar las temperaturas
    temperaturas = []

    # Solicita al usuario ingresar las temperaturas
    for i in range(1, 5):
        temperatura = float(input(f"Ingrese la temperatura {i}: "))
        temperaturas.append(temperatura)

    # Calcula el promedio de las temperaturas
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)

    # Muestra cada temperatura registrada y su valor
    print("\nTemperaturas registradas:")
    for i, temp in enumerate(temperaturas, start=1):
        print(f"Temperatura {i}: {temp}")

    # Muestra el promedio de las temperaturas
    print(f"\nEl promedio de las temperaturas es: {promedio}")

if __name__ == "__main__":
    main()
