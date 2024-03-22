# FUNDACION UNIVERSITARIA TECNOLOGICO COMFENALCO
# ACTIVIDAD DE PROGRAMACION
# PROGRAMA: Ingeniería Industrial
# DOCENTE: Ing. Alexander Diaz Chico
# ESTUDIANTE: Elkin Marrugo Elles.
def main():
    # Solicita al usuario ingresar los dos números
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo número: "))

    # Calcula la parte entera de la división de los números
    parte_entera = primer_numero // segundo_numero

    # Muestra los resultados
    print("\nResultados:")
    print("Primer número y su valor:", primer_numero)
    print("Segundo número y su valor:", segundo_numero)
    print("Parte entera de la división de los números y su valor:", parte_entera)

if __name__ == "__main__":
    main()
