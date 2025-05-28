# Sistema de Gestión de Empleados para Aeropuerto by JDRB && KAGG
import psycopg2
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

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

console = Console()

# ---------- CONEXIÓN ----------
def conectar():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="posgres",
        host="localhost",
        port="5432"
    )

def titulo(texto):
    console.print(Panel.fit(f"[bold cyan]{texto}[/bold cyan]", title="Gestión de Empleados", border_style="bright_blue"))

def listar_empleados():
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id_empleado, nombres, apellidos, documento, correo, telefono 
                FROM empleado ORDER BY id_empleado;
            """)
            empleados = cur.fetchall()

            if not empleados:
                console.print("[bold red]No hay empleados registrados.[/bold red]")
                return

            table = Table(title="Empleados Registrados", show_lines=True)

            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Nombres", style="green")
            table.add_column("Apellidos", style="green")
            table.add_column("Documento", style="yellow")
            table.add_column("Correo", style="magenta")
            table.add_column("Teléfono", style="blue")

            for emp in empleados:
                table.add_row(str(emp[0]), emp[1], emp[2], emp[3], emp[4], emp[5])

            console.print(table)

def agregar_empleado():
    try:
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
                console.print("[green]Empleado agregado exitosamente.[/green]")
    except Exception as e:
        console.print(f"[bold red]Error al agregar:[/bold red] {e}")

def actualizar_empleado():
    try:
        id_empleado = int(input("Ingrese el ID del empleado a actualizar: "))
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
                    console.print("[green]Empleado actualizado correctamente.[/green]")
                else:
                    console.print("[yellow]No se encontró un empleado con ese ID.[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al actualizar:[/bold red] {e}")

def eliminar_empleado():
    try:
        id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
        confirmar = input(f"¿Está seguro que desea eliminar al empleado con ID {id_empleado}? (s/n): ").lower()
        if confirmar != 's':
            console.print("[yellow]Operación cancelada.[/yellow]")
            return

        with conectar() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM empleado WHERE id_empleado = %s", (id_empleado,))
                
                if cur.rowcount > 0:
                    console.print("[green]Empleado eliminado correctamente.[/green]")
                else:
                    console.print("[yellow]No se encontró un empleado con ese ID.[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Error al eliminar:[/bold red] {e}")


def menu():
    while True:
        os.system('cls')
        titulo("Menú Principal")
        listar_empleados()
        print("\nOpciones:")
        print("1. Agregar empleado")
        print("2. Actualizar empleado")
        print("3. Eliminar empleado")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            actualizar_empleado()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            break
        else:
            console.print("[bold red]Opción inválida[/bold red]")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    limpiar_pantalla()
    menu()

