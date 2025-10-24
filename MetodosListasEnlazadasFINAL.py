class nodo:
    def __init__(self,data):
        self.data=data
        self.next=None

class Lista_Enlazada:
    def __init__(self):
        self.head=None
#1--------------------------------------------------
    def Agregar_al_inicio(self,data):
        new_node=nodo(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
#2--------------------------------------------------
    def Agregar_al_final(self,data):
        new_node=nodo(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None: #O simplemente while current.next
                current=current.next
            current.next=new_node
#3--------------------------------------------------
    def Agregar_en_la_mitad(self, data):
            new_node = nodo(data)

            if self.head is None:
                self.head = new_node
                return

            slow = self.head
            fast = self.head
            anterior_a_mitad = None

            while fast is not None and fast.next is not None:
                anterior_a_mitad = slow
                slow = slow.next
                fast = fast.next.next
            
            if anterior_a_mitad is None:
                new_node.next = self.head.next
                self.head.next = new_node
            else:
                anterior_a_mitad.next = new_node
                new_node.next = slow
#4--------------------------------------------------    
    def Agregar_en_posicion(self, data, posicion):
        new_node = nodo(data)

        if posicion < 0:
            print("La posición no puede ser negativa.")
            return

        if posicion == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        contador = 0

        while current is not None and contador < posicion - 1:
            current = current.next
            contador += 1

        if current is None:
            print(f"La posición {posicion} excede la longitud de la lista o la lista está vacía.")
            return

        new_node.next = current.next
        current.next = new_node
#5--------------------------------------------------        
    def Imprimir_Lista_Enlazada(self):
     current = self.head

     if current is None:
         print("Lista vacía")
         return

     while current is not None:
         print(f" {current.data} -->", end="")  # usamos f-string aquí
         current = current.next

     print(" NONE")  # indica el final de la lista
#6--------------------------------------------------
    def Eliminar_Nodo(self, data):
        actual = self.head
        previo = None
        #Se busca el dato a eliminar en la lista
        while actual and actual.data != data:
            previo = actual
            actual = actual.next
        #Si el dato a eliminar es el primero,
        #entonces se reasigna la cabeza de la lista
        if previo is None:
            if actual: # Added this check in case the list was empty or data not found
                self.head = actual.next
        elif actual:
            previo.next = actual.next
            # The line "actual.next = None" is not strictly necessary
            # in Python as garbage collection will handle it,
            # but I'll include it as it was in your provided code.
            actual.next = None
        else:
            print(f"Nodo con data {data} no encontrado")
#7--------------------------------------------------

    def Eliminar_al_inicio(self):
        if self.head is None:
            print("La lista esta vacia")
        else:
            self.head=self.head.next
#8--------------------------------------------------
    def Eliminar_al_final(self):
        if self.head is None:
            print("La lista esta vacia")
        if self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next.next is not None:
                current=current.next
            current.next=None
#9--------------------------------------------------
    def Existe_nodo(self,data):
        if self.head is None:
            print("La lista esta vacia")
        else:
            current=self.head
            while current is not None:
                if current.data==data:
                    return True
#10--------------------------------------------------
    def is_empty(self):
        return self.head == None  
#11--------------------------------------------------
    def get_last_node(self):
     temp = self.head
     while(temp.next is not None):
         temp = temp.next
     return temp.data
#12--------------------------------------------------
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
                if actual.data < siguiente.data: #Aqui ordena de mayor a menor por el <, pero si quisiera 
                                                 #ordenar de menor a mayor cambio el < por un >.
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
#13-------------------------------------------------
    def promedio_lista(self):
        """Calcula el promedio de los datos de los nodos en la lista enlazada."""
        if self.head is None:
            return 0  # El promedio de una lista vacía es 0, o podrías lanzar una excepción.

        current = self.head
        suma_total = 0
        conteo = 0

        while current is not None:
            # Se asume que los datos son numéricos (int o float)
            suma_total += current.data
            conteo += 1
            current = current.next

        # Evitar división por cero, aunque ya lo manejamos con el check de self.head
        if conteo > 0:
            return suma_total / conteo
        else:
            return 0
#-------------------------------------------------        
#MAIN
Mi_lista = Lista_Enlazada() # Instancia de la clase
Mi_lista.Agregar_al_inicio(1)
Mi_lista.Agregar_al_inicio(2)
Mi_lista.Agregar_al_inicio(3)

         
#Mi_lista.Eliminar_al_final()
Mi_lista.Imprimir_Lista_Enlazada()
print(f"Existe el 3? {Mi_lista.Existe_nodo(3)}")

# Test Eliminar_Nodo with value 1
Mi_lista.Eliminar_Nodo(1)
Mi_lista.Imprimir_Lista_Enlazada()                

Mi_lista.Agregar_en_posicion(8, 1)
Mi_lista.Agregar_en_la_mitad(9)
Mi_lista.Imprimir_Lista_Enlazada()  

# Test del nuevo método
promedio = Mi_lista.promedio_lista()
print(f"El promedio de la lista es: {promedio}") 