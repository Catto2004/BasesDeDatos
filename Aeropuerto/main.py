import psycopg2
import os

# ---------- CONEXIÓN ---------- JUAN
def conectar():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="posgres",
        host="localhost",
        port="5432"
    )

"""
# ---------- CONEXIÓN ---------- KEVIN
def conectar():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="ke010ga",
        host="localhost",
        port="5432"
    )
"""

def listar_empleados():
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM empleado;")
            for row in cur.fetchall():
                print(row)

def agregar_empleado():
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    documento = input("Documento: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")

    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO empleado (nombres, apellidos, documento, correo, telefono)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombres, apellidos, documento, correo, telefono))
            print("Empleado agregado exitosamente.")

def actualizar_empleado():
    try:
        id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))

        # Nuevos datos
        nombres = input("Nuevos nombres: ")
        apellidos = input("Nuevos apellidos: ")
        documento = input("Nuevo documento: ")
        correo = input("Nuevo correo: ")
        telefono = input("Nuevo teléfono: ")

        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE empleado
                    SET nombres = %s,
                        apellidos = %s,
                        documento = %s,
                        correo = %s,
                        telefono = %s
                    WHERE id_empleado = %s
                """, (nombres, apellidos, documento, correo, telefono, id_empleado))
                
                if cur.rowcount > 0:
                    print("Empleado actualizado correctamente.")
                else:
                    print("No se encontró un empleado con ese ID.")
    except Exception as e:
        print(f"Error al actualizar: {e}")

def eliminar_empleado():
    try:
        id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))

        confirmar = input(f"¿Está seguro que desea eliminar al empleado con ID {id_empleado}? (s/n): ").lower()
        if confirmar != 's':
            print("Operación cancelada.")
            return

        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM empleado WHERE id_empleado = %s", (id_empleado,))
                
                if cur.rowcount > 0:
                    print("Empleado eliminado correctamente.")
                else:
                    print("No se encontró un empleado con ese ID.")
    except Exception as e:
        print(f"Error al eliminar: {e}")


def menu():
    while True:
        print("\n--- Gestión de Empleados ---")
        print("1. Listar empleados")
        print("2. Agregar empleado")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado") 
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_empleados()
        elif opcion == "2":
            agregar_empleado()
        elif opcion == "3":
            actualizar_empleado()
        elif opcion == "4":
            eliminar_empleado()  # LLAMADO NUEVO
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    os.system("cls")
    menu()
