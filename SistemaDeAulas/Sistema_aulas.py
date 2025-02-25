def Guardar_aulas():
    print("Ingrese los datos de las aulas")
    codigo = input("Ingrese el codigo del aula: ").strip()
    largo = int(input("Ingrese el largo del aula: ").strip())
    ancho = int(input("Ingrese el ancho del aula: ").strip())
    capacidad = int(input("Ingrese la capacidad del aula: ").strip())
    color = input("Ingrese el color del aula: ").strip()
    tipo_aula = input("Ingrese el tipo de aula: ").strip()

    with open("Aulas.txt", "a", encoding="utf-8") as f:
        f.write(f"{codigo}, {largo}, {ancho}, {capacidad}, {color}, {tipo_aula}\n")
    print("Datos guardados correctamente")

#---------------------------------------------------

def Ver_aulas():
    with open("Aulas.txt", "r", encoding="utf-8") as f:
        print(f.read())

#---------------------------------------------------

def Consultar_aulas():
    codigo = input("Ingrese el cdigo del aula que desea buscar: ").strip()
    with open("Aulas.txt", "r", encoding="utf-8") as f:
        dato_buscar = f.readlines()
        for linea in dato_buscar:
            if codigo in linea:
                print(linea)
                break
        else:
            print("Aula no encontrada")
                
#---------------------------------------------------

def borrar_aulas():
    codigo = input("Ingrese el codigo del aula que desea borrar: ").strip()
    with open("Aulas.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    with open("Aulas.txt", "w", encoding="utf-8") as f:
        for linea in lineas:
            if codigo not in linea:
                f.write(linea)
            elif codigo in linea:
                aula_eliminada = linea
    with open("Aulas_eliminadas.txt", "a", encoding="utf-8") as f:
        f.write(aula_eliminada)
        print("Aula eliminada correctamente")

#------------------------------------------------------

def Actualizar_aulas():
    codigo = input("Ingrese el codigo del aula que desea actualizar: ").strip()
    with open("Aulas.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    with open("Aulas.txt", "w", encoding="utf-8") as f:
        for linea in lineas:
            if codigo in linea:
                largo = int(input("Ingrese el largo del aula: ").strip())
                ancho = int(input("Ingrese el ancho del aula: ").strip())
                capacidad = int(input("Ingrese la capacidad del aula: ").strip())
                color = input("Ingrese el color del aula: ").strip()
                tipo_aula = input("Ingrese el tipo de aula: ").strip()
                f.write(f"{codigo}, {largo}, {ancho}, {capacidad}, {color}, {tipo_aula}\n")
                print("Aula actualizada correctamente")
            else:
                f.write(linea)

def Recuperar_aula():
    codigo = input("Ingrese el codigo del aula que desea recuperar: ").strip()
    with open("Aulas_eliminadas.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    with open("Aulas_eliminadas.txt", "w", encoding="utf-8") as f:
        for linea in lineas:
            if codigo in linea:
                with open("Aulas.txt", "a", encoding="utf-8") as f:
                    f.write(linea)
                    print("Aula recuperada correctamente")
            else:
                f.write(linea) 

def Menu():
    print("1. Guardar aulas")
    print("2. Ver aulas")
    print("3. Consultar aulas")
    print("4. Borrar aulas")
    print("5. Actualizar aulas")
    print("6. Recuperar aula")
    print("7. Salir")
    opcion = input("Ingrese la opcion que desea realizar: ").strip()
    return opcion

def Sistema_aulas():
    while True:
        opcion = Menu()
        if opcion == "1":
            Guardar_aulas()
        elif opcion == "2":
            Ver_aulas()
        elif opcion == "3":
            Consultar_aulas()
        elif opcion == "4":
            borrar_aulas()
        elif opcion == "5":
            Actualizar_aulas()
        elif opcion == "6":
            Recuperar_aula()
        elif opcion == "7":
            print("Gracias por utilizar el sistema")
            break
        else:
            print("Opcion incorrecta")
 
if __name__ == "__main__":
   Sistema_aulas()

