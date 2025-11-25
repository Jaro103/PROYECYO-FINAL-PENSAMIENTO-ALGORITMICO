import json
import os

ARCHIVO = "estudiantes.json"

lista_estudiantes = []
lista_notas = []


def contar_elementos(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador


def obtener_suma_y_cantidad(lista):
    suma = 0
    cantidad = 0
    for x in lista:
        suma += x
        cantidad += 1
    return suma, cantidad


def buscar_estudiante(nombre):
    indice = 0
    for est in lista_estudiantes:
        if est == nombre:
            return indice
        indice += 1
    return -1


def cargar_desde_archivo():

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)

        # limpiamos y volvemos a llenar las listas
        lista_estudiantes.clear()
        lista_notas.clear()

        lista_estudiantes.extend(datos["estudiantes"])
        lista_notas.extend(datos["notas"])

        print("✅ Datos cargados correctamente.")
    else:
        print("ℹ️ No existe archivo, iniciando vacío.")


def guardar_en_archivo():
    datos = {
        "estudiantes": lista_estudiantes,
        "notas": lista_notas
    }

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print("✅ Datos guardados.")


def agregar_estudiante():
    nombre = input("Ingrese el nombre: ").strip().title()

    if buscar_estudiante(nombre) != -1:
        print("⚠️ Ese estudiante ya existe.")
        return

    lista_estudiantes.append(nombre)
    lista_notas.append([])
    print(f"✅ Estudiante '{nombre}' agregado.")


def agregar_notas():
    nombre = input("Nombre del estudiante: ").strip().title()
    pos = buscar_estudiante(nombre)

    if pos == -1:
        print("⚠️ Estudiante no encontrado.")
        return

    nota = float(input("Ingrese la nota (0.0 - 5.0): "))
    if 0 <= nota <= 5:
        lista_notas[pos].append(nota)
        print(f"✅ Nota {nota} agregada a {nombre}.")
    else:
        print("⚠️ Nota fuera de rango.")


def mostrar_estudiantes():
    if contar_elementos(lista_estudiantes) == 0:
        print("⚠️ No hay estudiantes.")
        return

    print("\n📋 Lista de estudiantes:")
    indice = 0
    for nombre in lista_estudiantes:
        notas = lista_notas[indice]
        suma, cantidad = obtener_suma_y_cantidad(notas)

        if cantidad > 0:
            promedio = suma / cantidad
            print(f"- {nombre}: {notas} -> Promedio: {promedio:.2f}")
        else:
            print(f"- {nombre}: sin notas registradas.")

        indice += 1


def calcular_promedio_general():
    total_suma = 0
    total_cantidad = 0

    for notas_est in lista_notas:
        suma, cantidad = obtener_suma_y_cantidad(notas_est)
        total_suma += suma
        total_cantidad += cantidad

    if total_cantidad == 0:
        print("⚠️ No hay notas en todo el curso.")
    else:
        print(f"📊 Promedio general: {total_suma / total_cantidad:.2f}")


def eliminar_estudiante():
    nombre = input("Ingrese el nombre a eliminar: ").strip().title()
    pos = buscar_estudiante(nombre)

    if pos == -1:
        print("⚠️ Estudiante no encontrado.")
        return

    confirm = input(f"¿Eliminar a {nombre}? (s/n): ").lower()
    if confirm == "s":
        lista_estudiantes.pop(pos)
        lista_notas.pop(pos)
        print(f"✅ {nombre} eliminado.")
    else:
        print("Operación cancelada.")


def menu():
    while True:
        print("""
====== SISTEMA DE NOTAS ESTUDIANTILES ======
1. Agregar estudiante
2. Agregar nota
3. Mostrar estudiantes y notas
4. Promedio general
5. Eliminar estudiante
6. Guardar datos
7. Cargar datos
8. Salir
============================================
""")
        op = input("Seleccione una opción (1-8): ").strip()

        if op == "1": agregar_estudiante()
        elif op == "2": agregar_notas()
        elif op == "3": mostrar_estudiantes()
        elif op == "4": calcular_promedio_general()
        elif op == "5": eliminar_estudiante()
        elif op == "6": guardar_en_archivo()
        elif op == "7": cargar_desde_archivo()
        elif op == "8":
            guardar_en_archivo()
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    cargar_desde_archivo()
    menu()

