class Tarea:
    def __init__(self, identificador, titulo, descripcion, estado):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                self.tareas.remove(tarea)
                break

    def buscar_tarea(self, identificador):
        for tarea in self.tareas:
            if tarea.identificador == identificador:
                return tarea
        return None

    def cambiar_estado_tarea(self, identificador, nuevo_estado):
        tarea = self.buscar_tarea(identificador)
        if tarea:
            tarea.estado = nuevo_estado

    def mostrar_tareas_ordenadas(self):
        tareas_ordenadas = sorted(self.tareas, key=lambda tarea: tarea.identificador)
        for tarea in tareas_ordenadas:
            print(f"ID: {tarea.identificador}, Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")


# Función para agregar una tarea
def agregar_tarea():
    identificador = int(input("Ingrese el identificador de la tarea: "))
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    estado = input("Ingrese el estado de la tarea (pendiente, en progreso, completada): ")
    tarea = Tarea(identificador, titulo, descripcion, estado)
    sistema.agregar_tarea(tarea)
    print("La tarea se agregó correctamente.")

# Función para eliminar una tarea
def eliminar_tarea():
    identificador = int(input("Ingrese el identificador de la tarea a eliminar: "))
    sistema.eliminar_tarea(identificador)
    print("La tarea se eliminó correctamente.")

# Función para buscar una tarea
def buscar_tarea():
    identificador = int(input("Ingrese el identificador de la tarea a buscar: "))
    tarea = sistema.buscar_tarea(identificador)
    if tarea:
        print(f"Tarea encontrada - ID: {tarea.identificador}, Título: {tarea.titulo}, Estado: {tarea.estado}")
    else:
        print("Tarea no encontrada.")

# Función para cambiar el estado de una tarea
def cambiar_estado_tarea():
    identificador = int(input("Ingrese el identificador de la tarea a modificar: "))
    nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
    sistema.cambiar_estado_tarea(identificador, nuevo_estado)
    print("El estado de la tarea se modificó correctamente.")

# Función para mostrar las tareas en orden ascendente según su identificador
def mostrar_tareas():
    sistema.mostrar_tareas_ordenadas()

# Crear instancia del sistema de gestión de tareas
sistema = SistemaGestionTareas()

while True:
    print("\n--- Gestión de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Buscar tarea")
    print("4. Cambiar estado de tarea")
    print("5. Mostrar tareas")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        buscar_tarea()
    elif opcion == "4":
        cambiar_estado_tarea()
    elif opcion == "5":
        mostrar_tareas()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
