from DataStructures.List import array_list as lt

def new_queue():
    # Crea una nueva cola vacía utilizando un array_list
    return lt.new_list()
def enqueue(my_queue, element):
    # Agrega un elemento al final de la cola
    lt.add_last(my_queue, element)
    return my_queue
def dequeue(my_queue):
    # Retira y devuelve el primer elemento de la cola
    if lt.size(my_queue) > 0:
        first_element = lt.first_element(my_queue)
        lt.remove_first(my_queue)
        return first_element
    else:
        return None
def peek(my_queue):
    # Devuelve el primer elemento de la cola sin eliminarlo
    return lt.first_element(my_queue)
def is_empty(my_queue):
    # Verifica si la cola está vacía
    return lt.is_empty(my_queue)
def size(my_queue):
    # Devuelve el tamaño de la cola
    return lt.size(my_queue)
