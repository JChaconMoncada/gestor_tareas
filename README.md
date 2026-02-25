# Sistema de Gestión de Tareas Personal

Una aplicación de línea de comandos (CLI) construida en Python para gestionar tareas diarias de forma eficiente, almacenando la información de manera persistente en un archivo JSON.

## Funcionalidades Principales
1. **Agregar tareas:** Permite ingresar título, descripción y fecha límite.
2. **Listar pendientes:** Visualiza rápidamente las tareas que aún no has terminado.
3. **Completar tareas:** Marca las tareas como completadas mediante un ID único generado automáticamente.

## Diagramas del Sistema

### Diagrama de Arquitectura
```mermaid
graph LR
    A[Usuario Consola] <--> B(main.py)
    B <--> C[(tareas.json)]

### Diagrama de Flujo (Agregar Tarea)

graph TD
    A[Inicio] --> B[Ingresar Datos]
    B --> C{Generar ID Único}
    C --> D[Guardar en JSON]
    D --> E[Mostrar Éxito]
    E --> F[Fin]