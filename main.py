import json
import os
import uuid

ARCHIVO_DATOS = 'tareas.json'

def cargar_tareas():
    """Carga las tareas del archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    with open(ARCHIVO_DATOS, 'r') as file:
        return json.load(file)

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_DATOS, 'w') as file:
        json.dump(tareas, file, indent=4)

def agregar_tarea(tareas, titulo, descripcion, fecha):
    """Lógica para agregar una tarea a la lista."""
    nueva_tarea = {
        "id": str(uuid.uuid4())[:8], # Genera un ID corto de 8 caracteres
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha": fecha,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    return tareas

def listar_pendientes(tareas):
    """Filtra y devuelve solo las tareas pendientes."""
    return [t for t in tareas if t['estado'] == 'pendiente']

def completar_tarea(tareas, id_tarea):
    """Busca una tarea por ID y la marca como completada."""
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['estado'] = 'completada'
            return True # Retorna True si la encontró y modificó
    return False

def menu():
    """Interfaz de consola para el usuario."""
    tareas = cargar_tareas()
    
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar nueva tarea")
        print("2. Ver tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            desc = input("Descripción: ")
            fecha = input("Fecha límite (DD/MM/AAAA): ")
            tareas = agregar_tarea(tareas, titulo, desc, fecha)
            guardar_tareas(tareas)
            print("✅ Tarea agregada con éxito.")
            
        elif opcion == '2':
            pendientes = listar_pendientes(tareas)
            print("\n--- TAREAS PENDIENTES ---")
            if not pendientes:
                print("No hay tareas pendientes. ¡Buen trabajo!")
            for t in pendientes:
                print(f"[{t['id']}] {t['titulo']} (Vence: {t['fecha']}) - {t['descripcion']}")
                
        elif opcion == '3':
            id_tarea = input("Ingresa el ID de la tarea a completar: ")
            if completar_tarea(tareas, id_tarea):
                guardar_tareas(tareas)
                print("✅ Tarea marcada como completada.")
            else:
                print("❌ Tarea no encontrada.")
                
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()