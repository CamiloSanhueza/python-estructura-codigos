class Video:
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration


class Node:
    def __init__(self, video):
        self.video = video
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def agregar_video(self, video):
        new_node = Node(video)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def mostrar_lista_videos(self):
        if self.is_empty():
            print("La lista de videos está vacía.")
        else:
            current = self.head
            while True:
                print("Título:", current.video.title)
                print("Autor:", current.video.author)
                print("Duración:", current.video.duration)
                print("-------------------------")
                current = current.next
                if current == self.head:
                    break

    def buscar_video(self, title):
        if self.is_empty():
            print("La lista de videos está vacía.")
        else:
            current = self.head
            while True:
                if current.video.title == title:
                    print("Video encontrado:")
                    print("Título:", current.video.title)
                    print("Autor:", current.video.author)
                    print("Duración:", current.video.duration)
                    break
                current = current.next
                if current == self.head:
                    print("Video no encontrado.")

    def eliminar_video(self, title):
        if self.is_empty():
            print("La lista de videos está vacía.")
        elif self.head.video.title == title:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        else:
            previous = self.head
            current = self.head.next
            while current != self.head:
                if current.video.title == title:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                    break
                previous = current
                current = current.next
            else:
                print("Video no encontrado.")


# Función para obtener datos del video desde el teclado
def obtener_datos_video():
    title = input("Ingrese el título del video: ")
    author = input("Ingrese el autor del video: ")
    duration = input("Ingrese la duración del video: ")
    return Video(title, author, duration)


# Ejemplo de uso
playlist = CircularLinkedList()

while True:
    print("\n------- MENÚ -------")
    print("1. Agregar video")
    print("2. Mostrar lista de videos")
    print("3. Buscar video")
    print("4. Eliminar video")
    print("5. Salir")
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        video = obtener_datos_video()
        playlist.agregar_video(video)
        print("Video agregado exitosamente.")

    elif opcion == "2":
        print("\nLista de videos:")
        playlist.mostrar_lista_videos()

    elif opcion == "3":
        title = input("Ingrese el título del video a buscar: ")
        playlist.buscar_video(title)

    elif opcion == "4":
        title = input("Ingrese el título del video a eliminar: ")
        playlist.eliminar_video(title)
        print("Video eliminado exitosamente.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1/2/3/4/5).")

