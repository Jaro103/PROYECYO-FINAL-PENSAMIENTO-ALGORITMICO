import json
import os

ARCHIVO = "estudiantes.json"
estudiantes = {}

def cargar_desde_archivo():
    """Carga el diccionario 'estudiantes' desde un archivo JSON si existe."""
    global estudiantes
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                estudiantes = json.load(f)
            # json carga listas y números, pero si alguna nota fue guardada como entero,
            # al calcular promedios se aceptan igual. Aseguramos listas:
            for k, v in estudiantes.items():
                if not isinstance(v, list):
                    estudiantes[k] = list(v) if v is not None else []
            print(f"✅ Datos cargados desde '{ARCHIVO}'.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️ Error al leer '{ARCHIVO}': {e}. Se iniciará con datos vacíos.")
            estudiantes = {}
    else:
        print(f"ℹ️ No existe '{ARCHIVO}'. Se iniciará con datos vacíos.")

def guardar_en_archivo():
    """Guarda el diccionario 'estudiantes' en un archivo JSON."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(estudiantes, f, ensure_ascii=False, indent=4)
        print(f"✅ Datos guardados en '{ARCHIVO}'.")
    except IOError as e:
        print(f"⚠️ No se pudo guardar en '{ARCHIVO}': {e}")

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if not nombre:
        print("⚠️ Nombre vacío.")
        return
    if nombre in estudiantes:
        print("⚠️ El estudiante ya existe.")
    else:
        estudiantes[nombre] = []
        print(f"✅ Estudiante '{nombre}' agregado correctamente.")

def agregar_notas():
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if nombre in estudiantes:
        try:
            nota = float(input("Ingrese la nota del estudiante (0.0 - 5.0): ").strip())
            if 0.0 <= nota <= 5.0:
                estudiantes[nombre].append(nota)
                print(f"✅ Nota {nota} agregada a {nombre}.")
            else:
                print("⚠️ La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido.")
    else:
        print("⚠️ Estudiante no encontrado.")

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("⚠️ No hay estudiantes registrados.")
    else:
        print("\n📋 Lista de estudiantes y sus notas:")
        for nombre, notas in estudiantes.items():
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"- {nombre}: Notas = {notas}, Promedio = {promedio:.2f}")
            else:
                print(f"- {nombre}: sin notas registradas.")

def calcular_promedio_general():
    total_notas = 0
    cantidad_notas = 0
    for notas in estudiantes.values():
        total_notas += sum(notas)
        cantidad_notas += len(notas)
    if cantidad_notas == 0:
        print("⚠️ No hay notas registradas para calcular el promedio general.")
    else:
        promedio_general = total_notas / cantidad_notas
        print(f"📊 Promedio general del curso: {promedio_general:.2f}")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
    if nombre in estudiantes:
        confirm = input(f"¿Eliminar a {nombre}? (s/n): ").strip().lower()
        if confirm == "s":
            estudiantes.pop(nombre)
            print(f"✅ Estudiante {nombre} eliminado.")
        else:
            print("Operación cancelada.")
    else:
        print("⚠️ Estudiante no encontrado.")

def menu():
    while True:
        print("""
====== SISTEMA DE NOTAS ESTUDIANTILES ======
1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes y notas
4. Calcular promedio general
5. Eliminar estudiante
6. Guardar datos en archivo
7. Cargar datos desde archivo
8. Salir
============================================
""")
        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_notas()
        elif opcion == "3":
            mostrar_estudiantes()
        elif opcion == "4":
            calcular_promedio_general()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "6":
            guardar_en_archivo()
        elif opcion == "7":
            cargar_desde_archivo()
        elif opcion == "8":
            # Guardar automáticamente antes de salir
            guardar_en_archivo()
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    cargar_desde_archivo()
    menu()
