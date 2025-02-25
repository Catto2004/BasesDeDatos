import os

# Archivo donde se almacenan los registros de aulas.
ARCHIVO_AULAS = "aulas.txt"

def formatear_campo(texto, longitud):
    """Asegura que el campo de texto tenga la longitud indicada."""
    return texto.strip().ljust(longitud)[:longitud]

def agregar_registro():
    codigo = formatear_campo(input("Ingrese el codigo del aula (max 10 caracteres): "), 10)
    try:
        largo = float(input("Ingrese el largo: "))
        ancho = float(input("Ingrese el ancho: "))
        capacidad = int(input("Ingrese la capacidad: "))
    except ValueError:
        print("Error: Ingrese valores numericos validos para largo, ancho y capacidad.")
        return
    color = formatear_campo(input("Ingrese el color (max 20 caracteres): "), 20)
    try:
        tipo_aula = int(input("Ingrese el tipo de aula (valor entero corto): "))
    except ValueError:
        print("Error: Ingrese un valor entero para el tipo de aula.")
        return

    # Se arma el registro, se convierten los numeros a string para concatenar.
    registro = f"{codigo}|{largo}|{ancho}|{capacidad}|{color}|{tipo_aula}\n"
    
    # Se escribe el registro al final del archivo.
    with open(ARCHIVO_AULAS, "a") as f:
        f.write(registro)
    print("Registro agregado exitosamente.")

def listar_registros():
    print("\n--- Listado de Aulas ---")
    if not os.path.exists(ARCHIVO_AULAS):
        print("No hay registros.")
        return
    with open(ARCHIVO_AULAS, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                campos = linea.split("|")
                # Se muestran los campos formateados
                print(f"Codigo: {campos[0].strip()}, Largo: {campos[1]}, Ancho: {campos[2]}, Capacidad: {campos[3]}, Color: {campos[4].strip()}, Tipo: {campos[5]}")
    print("-------------------------\n")

def buscar_registro_por_codigo():
    codigo_buscar = formatear_campo(input("Ingrese el codigo del aula a buscar: "), 10)
    encontrado = False
    if not os.path.exists(ARCHIVO_AULAS):
        print("No hay registros.")
        return
    with open(ARCHIVO_AULAS, "r") as f:
        for linea in f:
            if linea.startswith(codigo_buscar):
                campos = linea.strip().split("|")
                print(f"Registro encontrado: Codigo: {campos[0].strip()}, Largo: {campos[1]}, Ancho: {campos[2]}, Capacidad: {campos[3]}, Color: {campos[4].strip()}, Tipo: {campos[5]}")
                encontrado = True
                break
    if not encontrado:
        print("Registro no encontrado.")

def eliminar_registro():
    codigo_eliminar = formatear_campo(input("Ingrese el codigo del aula a eliminar: "), 10)
    if not os.path.exists(ARCHIVO_AULAS):
        print("No hay registros.")
        return
    # Se crea un archivo temporal para escribir los registros que no se eliminan
    with open(ARCHIVO_AULAS, "r") as f, open("temp.txt", "w") as temp:
        eliminado = False
        for linea in f:
            if linea.startswith(codigo_eliminar):
                eliminado = True
                continue  # se omite el registro a eliminar
            temp.write(linea)
    os.replace("temp.txt", ARCHIVO_AULAS)
    if eliminado:
        print("Registro eliminado exitosamente.")
    else:
        print("Registro no encontrado.")

def actualizar_registro():
    codigo_actualizar = formatear_campo(input("Ingrese el codigo del aula a actualizar: "), 10)
    if not os.path.exists(ARCHIVO_AULAS):
        print("No hay registros.")
        return
    actualizado = False
    with open(ARCHIVO_AULAS, "r") as f, open("temp.txt", "w") as temp:
        for linea in f:
            if linea.startswith(codigo_actualizar):
                print("Ingrese los nuevos datos para el aula:")
                nuevo_codigo = formatear_campo(input("Nuevo codigo (max 10 caracteres): "), 10)
                try:
                    nuevo_largo = float(input("Nuevo largo: "))
                    nuevo_ancho = float(input("Nuevo ancho: "))
                    nueva_capacidad = int(input("Nueva capacidad: "))
                except ValueError:
                    print("Error en la conversion de datos numericos. Registro no actualizado.")
                    temp.write(linea)
                    continue
                nuevo_color = formatear_campo(input("Nuevo color (max 20 caracteres): "), 20)
                try:
                    nuevo_tipo = int(input("Nuevo tipo de aula (valor entero corto): "))
                except ValueError:
                    print("Error en la conversion de datos para el tipo. Registro no actualizado.")
                    temp.write(linea)
                    continue
                nuevo_registro = f"{nuevo_codigo}|{nuevo_largo}|{nuevo_ancho}|{nueva_capacidad}|{nuevo_color}|{nuevo_tipo}\n"
                temp.write(nuevo_registro)
                actualizado = True
            else:
                temp.write(linea)
    os.replace("temp.txt", ARCHIVO_AULAS)
    if actualizado:
        print("Registro actualizado exitosamente.")
    else:
        print("Registro no encontrado.")

def importar_registros():
    ruta_importar = input("Ingrese la ruta del archivo a importar: ")
    if not os.path.exists(ruta_importar):
        print("El archivo no existe.")
        return
    with open(ruta_importar, "r") as f_import, open(ARCHIVO_AULAS, "a") as f_aulas:
        for linea in f_import:
            # Se podria validar la estructura de la linea si es necesario.
            f_aulas.write(linea)
    print("Importacion completada.")

def exportar_registros():
    nombre_exportar = input("Ingrese el nombre del archivo de exportacion: ")
    with open(ARCHIVO_AULAS, "r") as f_aulas, open(nombre_exportar, "w") as f_export:
        for linea in f_aulas:
            f_export.write(linea)
    print("Exportacion completada.")

def menu():
    opciones = {
        "1": ("Agregar registro", agregar_registro),
        "2": ("Eliminar registro", eliminar_registro),
        "3": ("Actualizar registro", actualizar_registro),
        "4": ("Listar registros", listar_registros),
        "5": ("Buscar registro por codigo", buscar_registro_por_codigo),
        "6": ("Importar registros desde archivo", importar_registros),
        "7": ("Exportar registros a archivo", exportar_registros),
        "8": ("Salir", None)
    }
    while True:
        print("\n--- Menu de Aulas ---")
        for clave, (desc, _) in opciones.items():
            print(f"{clave}. {desc}")
        opcion = input("Seleccione una opcion: ")
        if opcion == "8":
            print("Saliendo del programa...")
            break
        accion = opciones.get(opcion, (None, None))[1]
        if accion:
            accion()
        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
