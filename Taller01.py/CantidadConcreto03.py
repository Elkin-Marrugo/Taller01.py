# FUNDACION UNIVERSITARIA TECNOLOGICO COMFENALCO
# ACTIVIDAD DE PROGRAMACION
# PROGRAMA: Ingeniería Industrial
# DOCENTE: Ing. Alexander Diaz Chico
# ESTUDIANTE: Elkin Marrugo Elles.
def main():


    # Solicita al usuario ingresar los datos para cada tramo
    while True:
        # Solicita los datos para el tramo actual
        nombre_ingeniero = input("Ingrese el nombre del ingeniero a cargo: ")
        nombre_tramo = input("Ingrese el nombre del tramo: ")
        longitud_tramo = float(input("Ingrese la longitud del tramo (en metros): "))
        ancho_tramo = float(input("Ingrese el ancho del tramo (en metros): "))
        espesor_pavimento = float(input("Ingrese el espesor del pavimento (en metros): "))
        
        # Calcula el volumen de concreto requerido
        volumen_concreto = longitud_tramo * ancho_tramo * espesor_pavimento
        
        # Muestra los resultados
        print("\nResultados:")
        print("Nombre del ingeniero a cargo:", nombre_ingeniero)
        print("Nombre del tramo:", nombre_tramo)
        print("Cantidad de concreto requerido (m³) para el tramo:", volumen_concreto)
        
        # Pregunta al usuario si desea procesar otro tramo
        continuar = input("\n¿Desea procesar otro tramo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
