#Ejercicio Festival de Talentos
import random

# LISTA ENLAZADA (Información y Puntajes)
class nodo_ListaEnlazada:
    def __init__(self, nombre, edad, puntaje):
        self.nombre = nombre
        self.edad = edad
        self.puntaje = puntaje
        self.next = None
        
class ListaEnlazada:
    def __init__(self):
        self.head = None
        
    def add_Participante(self, nombre, edad, puntaje=0):
        new_node = nodo_ListaEnlazada(nombre, edad, puntaje)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def Imprimir_Lista_Enlazada(self):
        current = self.head
        if current is None:
            print("Lista vacía")
            return
        while current is not None:
            print(f" {current.nombre}, {current.edad}, Puntaje Acumulado: {current.puntaje} -->", end="")
            current = current.next
        print(" NONE")

    def acumular_puntaje(self, nombre, puntos):
        current = self.head
        while current is not None:
            if current.nombre == nombre:
                current.puntaje += puntos
                return
            current = current.next
            
    def ordenar_lista(self):
        # Ordenamiento de mayor a menor puntaje
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
                    
    def Eliminar_ultimo(self):
        # Elimina el último nodo (el de menor puntaje después de ordenar)
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

#----------------------------------------------------------

# LISTA CIRCULAR (Orden de Presentación)
class nodo_ListaCircular:
    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 0
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def add_nombre(self, nombre):
        node = nodo_ListaCircular(nombre)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def Imprimir_Lista_Circular(self):
        if self.is_empty():
            print("Lista vacía")
            return
        current = self.head
        print(f"{current.nombre} -->", end="")
        current = current.next
        while current != self.head:
            print(f" {current.nombre} -->", end="")
            current = current.next
        print(" HEAD")

    def mover_al_inicio(self, nombre):
        if self.is_empty() or self.head.nombre == nombre:
            return

        current = self.head
        anterior = None
        
        # 1. Buscar y desconectar el nodo
        while current.nombre != nombre:
            anterior = current
            current = current.next
            if current == self.head:
                return

        anterior.next = current.next 

        # 2. Insertar al inicio (actualizar HEAD y cola)
        cola = self.head
        while cola.next != self.head:
            cola = cola.next
        
        cola.next = current
        current.next = self.head
        self.head = current
        
    def recorrer(self, rondas, lista_info):
        for ronda in range(1, rondas + 1):
            num_participantes = self.length()
            actual = self.head

            print(f"\n--- Ronda {ronda} ---")
            
            for i in range(num_participantes):
                nombre = actual.nombre
                
                print(f"Es el turno de {nombre}. ¿Está presente? (S/N):")
                # Simulación de respuesta "S" o "N"
                presente = random.choice("SN")
                print(f"Respuesta: {presente}")

                # --- Lógica de Asignación de Puntaje y Movimiento ---
                if presente == "S":
                    puntos = random.randint(1, 10)
                    print(f"  {nombre} obtuvo {puntos} puntos. ✅")
                    lista_info.acumular_puntaje(nombre, puntos)
                    
                    # Avanza al siguiente participante en el orden actual
                    actual = actual.next 

                else: # presente == "N"
                    puntos = 0
                    print(f"  {nombre} obtuvo {puntos} puntos por inasistencia. 🚫")
                    lista_info.acumular_puntaje(nombre, puntos)

                    # 1. Guardar el nodo del participante que sigue
                    siguiente_turno_node = actual.next
                    
                    # 2. Mover al jugador ausente (actual) al inicio (HEAD). Esto actualiza self.head.
                    self.mover_al_inicio(nombre)
                    
                    # 3. El siguiente turno debe ser para el participante que estaba después del ausente.
                    actual = siguiente_turno_node 

            print(f"\nOrden de la Lista Circular al final de la Ronda {ronda}:")
            self.Imprimir_Lista_Circular()
            print("Puntajes Acumulados:")
            lista_info.Imprimir_Lista_Enlazada()

#----------------------------------------------------------

# MAIN (Simulación)

# 1. Inicializar Participantes (Lista Enlazada)
Lista_Enlazada = ListaEnlazada()
participantes_info = [
    ("Juan", 25), 
    ("Maria", 24), 
    ("Pedro", 23), 
    ("Alberto", 22), 
    ("Laura", 21)
]

for nombre, edad in participantes_info:
    Lista_Enlazada.add_Participante(nombre, edad, puntaje=0)

print("--- Participantes Iniciales (Lista Enlazada) ---")
Lista_Enlazada.Imprimir_Lista_Enlazada() 

# 2. Inicializar Orden de Presentación (Lista Circular)
Lista_Circular = ListaCircular()
lista_participantes = [info[0] for info in participantes_info]
random.shuffle(lista_participantes) # Orden de presentación aleatorio inicial

for nombre in lista_participantes:
    Lista_Circular.add_nombre(nombre)

print("\n--- Orden Inicial de Presentación (Lista Circular) ---")
Lista_Circular.Imprimir_Lista_Circular()

# 3. Simulación del Festival (3 Rondas)
print("\n#############################################")
print("### INICIO DEL FESTIVAL DE TALENTOS (3 Rondas) ###")
print("#############################################")

Lista_Circular.recorrer(3, Lista_Enlazada)

# 4. Resultados Finales
print("\n#############################################")
print("### RESULTADOS FINALES ###")
print("#############################################")

# A. Ordenar la lista de información por puntaje (Mayor a Menor)
Lista_Enlazada.ordenar_lista()

print("CLASIFICACIÓN FINAL (Puntaje Acumulado):")
Lista_Enlazada.Imprimir_Lista_Enlazada()

# B. Anunciar al ganador
ganador = Lista_Enlazada.head
if ganador:
    print(f"\n¡EL GANADOR DEL FESTIVAL ES: {ganador.nombre} con un puntaje final de {ganador.puntaje}!")
    
# C. Eliminar los 2 últimos puntajes (los 2 peores)
Lista_Enlazada.Eliminar_ultimo()
Lista_Enlazada.Eliminar_ultimo()

print("\nLista de Participantes después de eliminar los 2 puntajes más bajos:")
Lista_Enlazada.Imprimir_Lista_Enlazada()