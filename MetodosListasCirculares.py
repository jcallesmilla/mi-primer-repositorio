class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
     

class Lista_Circular(object):

    def __init__(self):
        self.head = None
#1--------------------------------------------------
    def is_empty(self):
        return self.head is None
#2--------------------------------------------------
    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            # Si el siguiente nodo del nodo actual es el nodo principal, significa que este nodo es el nodo de cola
            # Si no, mueva el puntero hacia atrás
            if current.next == self.head:
                break
            else:
                current = current.next
        return count
#3--------------------------------------------------
    def imprimir(self):
        if self.is_empty():
            print("Lista vacía")
            return

        current = self.head
        print(f"{current.data} -->", end="")  # usamos f-string para el primer nodo
        current = current.next

        # Recorremos hasta volver al inicio
        while current != self.head:
            print(f" {current.data} -->", end="")  # espacio bonito y f-string
            current = current.next

        print(" HEAD")  # indica que se cerró el ciclo

#4--------------------------------------------------
    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            current = self.head
            # Mueva el puntero al nodo de cola
            while current.next is not self.head:
                current = current.next
            # El nodo de cola apunta al nuevo nodo
            current.next = node
            # El nuevo nodo apunta al nodo principal original
            node.next = self.head
            # Luego dele el título del nodo principal al nuevo nodo
            self.head = node

#5--------------------------------------------------
    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            current = self.head
            # Mueve el puntero al final
            while current.next is not self.head:
                current = current.next
            # El nodo de cola apunta al nuevo nodo
            current.next = node
            # El nuevo nodo apunta al nodo principal
            node.next = self.head

#6--------------------------------------------------
    def insert_node(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length():
            print ("Posición de inserción incorrecta")
            return False
        elif index == 0:
            self.add_first(data)
        elif index == self.length():
            self.add_last(data)
        else:
            current = self.head
            anterior = None # anterior es el nodo previo al nodo actual
            count = 0
            # Mueva el puntero a la posición para insertar
            while count < index:
                anterior = current
                current = current.next
                count += 1
            anterior.next = node
            node.next = current

#7--------------------------------------------------
    def remove_node(self, data):
        if self.is_empty():
            return
        # Si el nodo que se va a eliminar es el nodo principal
        elif data == self.head.data:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            anterior = None
            # Mover a la posición del nodo que se va a eliminar
            while current.data != data:
                anterior = current
                current = current.next
            # Apunte el nodo previo al nodo posterior, eliminando el nodo central
            anterior.next = current.next

#8--------------------------------------------------
    def remove2_node(self, data):
        if self.is_empty():
            return
        # Si el nodo que se va a eliminar es el nodo principal
        elif data == self.head.data:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            anterior = None
            while current.data != data:
                anterior = current
                current = current.next
            anterior.next = anterior.next.next

#9--------------------------------------------------
    def mover_al_inicio(self, data):
        if self.is_empty():
            return

        # Si ya es el nodo principal, no hacer nada
        if self.head.data == data:
            return

        current = self.head
        anterior = None

        # Buscar el nodo
        while current.data != data:
            anterior = current
            current = current.next
            if current == self.head:  # No encontrado
                print("Nodo no encontrado")
                return

        # Desconectar el nodo
        anterior.next = current.next

        # Insertar al inicio
        cola = self.head
        while cola.next != self.head:
            cola = cola.next
        cola.next = current
        current.next = self.head
        self.head = current

#10--------------------------------------------------
    def mover_al_final(self, data):
        if self.is_empty():
            return

        # Si la lista tiene un solo nodo o el nodo ya es el último, no hacer nada
        if self.head.next == self.head:
            return

        current = self.head
        anterior = None

        # Buscar el nodo
        while current.data != data:
            anterior = current
            current = current.next
            if current == self.head:  # No encontrado
                print("Nodo no encontrado")
                return

        # Si el nodo ya es el último (apunta al head), no hacer nada
        cola = self.head
        while cola.next != self.head:
            cola = cola.next
        if current == cola:
            return

        # Desconectar el nodo
        if current == self.head:
            # Si es el head, actualizar el head
            self.head = current.next
        else:
            anterior.next = current.next

        # Insertar al final
        cola.next = current
        current.next = self.head

#11--------------------------------------------------
    def mover_a_posicion(self, data, index):
            longitud = self.length()
            if self.is_empty() or index < 0 or index >= longitud:
                if self.is_empty():
                    print("Lista vacía, no se puede mover.")
                elif index < 0 or index >= longitud:
                    print(f"Posición de movimiento incorrecta. Debe ser entre 0 y {longitud - 1}.")
                return

            if index == 0:
                self.mover_al_inicio(data)
                return

            current = self.head
            anterior = None
            nodo_a_mover = None
            
            while True:
                if current.data == data:
                    nodo_a_mover = current
                    break
                anterior = current
                current = current.next
                if current == self.head: 
                    print("Nodo no encontrado para mover")
                    return

            if longitud == 1:
                return

            if nodo_a_mover == self.head:
                self.head = nodo_a_mover.next
                cola = self.head
                while cola.next != nodo_a_mover: 
                    cola = cola.next
                cola.next = self.head 
            else:
                anterior.next = nodo_a_mover.next

            current = self.head 
            anterior = None
            count = 0
            
            while count < index:
                anterior = current
                current = current.next 
                count += 1
            
            anterior.next = nodo_a_mover
            nodo_a_mover.next = current
            

#12--------------------------------------------------  
    def remover_duplicados(self):
            if self.is_empty():
                return
            
            current = self.head
            
            while True:
                if current is None:
                    break
                    
                corredor = current.next
                anterior_corredor = current
                
                while corredor != self.head:
                    if corredor.data == current.data:
                        anterior_corredor.next = corredor.next
                        corredor = corredor.next
                    else:
                        anterior_corredor = corredor
                        corredor = corredor.next

                if current.next == self.head:
                    break
                current = current.next   
#--------------------------------------------------                   
#Main
Lista1=Lista_Circular()
Lista1.add_last(2)
Lista1.add_first('Hola')
Lista1.add_first('Hola')
Lista1.add_first('Hola')
Lista1.add_first('Hola')
Lista1.add_first(0)
Lista1.add_last(3)
Lista1.imprimir()

Lista1.insert_node(1, 'Mundo')
Lista1.mover_al_inicio(3)
Lista1.mover_al_final("Mundo")
Lista1.mover_a_posicion(2, 1)
Lista1.remover_duplicados()
Lista1.imprimir()

Lista1.remove_node(0)
Lista1.imprimir()