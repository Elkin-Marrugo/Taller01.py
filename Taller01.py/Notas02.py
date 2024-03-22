# FUNDACION UNIVERSITARIA TECNOLOGICO COMFENALCO
# ACTIVIDAD DE PROGRAMACION
# PROGRAMA: Ingeniería Industrial
# DOCENTE: Ing. Alexander Diaz Chico
# ESTUDIANTE: Elkin Marrugo Elles.
def calcular_nota_definitiva(datos_estudiante):


    # Calcula la nota definitiva
    nota_definitiva = (datos_estudiante["corte1"] * 0.3) + (datos_estudiante["corte2"] * 0.3) + (datos_estudiante["corte3"] * 0.4)
    
    # Muestra los resultados
    print("Resultados:")
    print("Nombre del estudiante:", datos_estudiante["nombre"])
    print("Nombre de la asignatura:", datos_estudiante["asignatura"])
    print("Nota del primer corte:", datos_estudiante["corte1"])
    print("Nota del segundo corte:", datos_estudiante["corte2"])
    print("Nota del tercer corte:", datos_estudiante["corte3"])
    print("Nota definitiva:", nota_definitiva)

def main():
    # Solicita al usuario ingresar los datos
    datos_estudiante = {}
    datos_estudiante["nombre"] = input("Ingrese el nombre del estudiante: ")
    datos_estudiante["asignatura"] = input("Ingrese el nombre de la asignatura: ")
    datos_estudiante["corte1"] = float(input("Ingrese la nota del primer corte: "))
    datos_estudiante["corte2"] = float(input("Ingrese la nota del segundo corte: "))
    datos_estudiante["corte3"] = float(input("Ingrese la nota del tercer corte: "))

    # Calcula la nota definitiva
    calcular_nota_definitiva(datos_estudiante)

if __name__ == "__main__":
    main()
