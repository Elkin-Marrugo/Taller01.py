# FUNDACION UNIVERSITARIA TECNOLOGICO COMFENALCO
# ACTIVIDAD DE PROGRAMACION
# PROGRAMA: Ingeniería Industrial
# DOCENTE: Ing. Alexander Diaz Chico
# ESTUDIANTE: Elkin Marrugo Elles.
def main():
    # Solicita al usuario ingresar los dos números
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))

    # Calcula el residuo de la división de los números
    residuo = primer_numero % segundo_numero

    # Muestra los resultados
    print("\nResultados:")
    print("Primer número y su valor:", primer_numero)
    print("Segundo número y su valor:", segundo_numero)
    print("Residuo de los números:", residuo)

if __name__ == "__main__":
    main()
