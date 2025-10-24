# Nodo para lista enlazada simple
class NodoSimple:
  def __init__(self, nombre, edad, puntaje=0):
    self.nombre = nombre
    self.edad = edad
    self.puntaje = puntaje
    self.next = None

     

import random

# Lista enlazada simple
class ListaSimple:
    def __init__(self):
        self.head = None

    #inserta un NodoSimple al final de la lista
    def agregar_participante(self, nombre, edad):
        nuevo = NodoSimple(nombre, edad)
        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    #Busca el nombre en la lista y suma los puntos en el atributo puntaje.
    def acumular_puntaje(self, nombre, puntos):
        actual = self.head
        while actual:
            if actual.nombre == nombre:
                actual.puntaje += puntos
                return
            actual = actual.next
        #Otra opción para escribir el código
        '''
        while actual.next != None and actual.nombre != nombre:
            actual = actual.next
        if actual.nombre == nombre:
            actual.puntaje += puntos
            #actual.puntaje = actual.puntaje + puntos
        '''


    def ordenar_lista(self):
        if self.head is None or self.head.next is None:
            return

        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.head
            anterior = None
            while actual.next:
                siguiente = actual.next
                if actual.puntaje < siguiente.puntaje:
                    cambiado = True
                    if anterior is None:
                        self.head = siguiente
                    else:
                        anterior.next = siguiente
                    actual.next = siguiente.next
                    siguiente.next = actual
                    anterior = siguiente
                else:
                    anterior = actual
                    actual = actual.next
        #retorna el ganador
        return self.head


    # Método para eleminar el último nodo
    def delete_last(self):
        actual = self.head
        previo = None
        #Se llega al final de la lista
        while actual.next:
            previo = actual
            actual = actual.next
        #Si el dato a eliminar es el primero,
        #entonces se reasigna la cabeza de la lista

        if previo is None:
            self.head = actual.next
        elif actual:
            previo.next = actual.next
            actual.next = None

        #otra opción para eliminar
        '''
        actual = self.head
        while actual.next.next:  # busca el penúltimo
            actual = actual.next
        actual.next = None
        '''


    def mostrar_lista(self):
        actual = self.head
        while actual:
            print(f"{actual.nombre} - Edad: {actual.edad} - Puntaje: {actual.puntaje}")
            actual = actual.next


     

# Nodo para lista circular
class NodoCircular:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
     

# Lista circular
class ListaCircular:
    def __init__(self):
        self.head = None

    #Agregar nodos al final de la lista circular
    def agregar(self, nombre):
        nuevo = NodoCircular(nombre)
        if self.head is None:
            self.head = nuevo
            nuevo.next = nuevo
        else:
            actual = self.head
            while actual.next != self.head:
                actual = actual.next
            actual.next = nuevo
            nuevo.next = self.head

    def mover_al_final(self, nombre):
        if self.head is None:
            return

        anterior = None
        actual = self.head
        while True:
            if actual.nombre == nombre:
                break
            anterior = actual
            actual = actual.next
            if actual == self.head:
                return

        if actual == self.head:
            self.head = actual.next

            #temp.next = self.head
        else:
            anterior.next = actual.next
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = actual
            actual.next = self.head

    def imprimir_circular(self):

      if self.head == None:
          return
      cur = self.head
      print(f"\n {cur.nombre}", end = "-->")
      while cur.next != self.head:
          cur = cur.next
          print(cur.nombre, end = "-->")


    def recorrer(self, rondas, lista_info):
        #si se deja esta instrucción acá, entonces no se actualiza la ronda en
        #la cabeza de la lista, hay que ponerla dentro del for.
        #actual = self.head
        for ronda in range(1, rondas + 1):
            #En cada ronda se coloca la variable "actual" nuevamente en la cabeza
            actual = self.head
            print(f"\n--- Ronda {ronda} ---")
            contador = 0
            while contador < 5:
                nombre = actual.nombre
                print(f"Es el turno de {nombre}. ¿Está presente? (S/N):")
                presente = random.choice("SN")
                print(f"Respuesta automática: {presente}")

                if presente == "S":
                    puntos = random.randint(1, 10)
                    print(f"{nombre} obtuvo {puntos} puntos.")
                    lista_info.acumular_puntaje(nombre, puntos)
                    #avanzar al siguiente nodo
                    actual = actual.next
                else:
                    print(f"{nombre} fue movido al final por inasistencia.")
                    #avanzar al siguiente nodo antes de mover el nodo actual
                    actual = actual.next
                    self.mover_al_final(nombre)

                #Si esta instrucción (actual = actual.next) se deja aquí,
                #cuando hay un movimiento de
                #nodos, repite al jugador siguiente. Por esto se cambió esta
                #instrucción dentro del "else" y antes del movimiento del nodo.
                #Para garantizar que también avance en la condición "S", también
                #se copió allí.

                #actual = actual.next
                contador += 1
            self.imprimir_circular()

     

# MAIN
if __name__ == "__main__":


    lista_participantes = ListaSimple()
    lista_orden = ListaCircular()

    lista_participantes.agregar_participante("Ana", 19)
    lista_orden.agregar("Ana")

    lista_participantes.agregar_participante("Carlos", 21)
    lista_orden.agregar("Carlos")

    lista_participantes.agregar_participante("Luis", 20)
    lista_orden.agregar("Luis")

    lista_participantes.agregar_participante("María", 18)
    lista_orden.agregar("María")

    lista_participantes.agregar_participante("Juan", 22)
    lista_orden.agregar("Juan")

    print("\n--- Lista de Participantes ---")
    lista_participantes.mostrar_lista()
    lista_orden.imprimir_circular()


    lista_orden.recorrer(3, lista_participantes)

    print("\n--- Resultados Finales ---")
    lista_participantes.mostrar_lista()
    ganador = lista_participantes.ordenar_lista()

    print(f"\nGanador del Festival: {ganador.nombre} con {ganador.puntaje} puntos")
    lista_participantes.mostrar_lista()
    print("Se van a eliminar los 2 últimos jugadores")

    ##elimina los 2 últimos jugadores y muestra la lista
    lista_participantes.delete_last()
    lista_participantes.delete_last()
    print("\nParticipantes restantes:")
    lista_participantes.mostrar_lista()