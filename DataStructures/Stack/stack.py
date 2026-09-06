from DataStructures.List import array_list as lt
def new_stack():
    # Crea una nueva pila vacía utilizando un array_list
    return lt.new_list()
def push(my_stack, element):
    # Agrega un elemento al final de la pila
    lt.add_last(my_stack, element)
    return my_stack
def pop(my_stack):
    # Retira y devuelve el último elemento de la pila
    if lt.size(my_stack) > 0:
        last_element = lt.last_element(my_stack)
        lt.remove_last(my_stack)
        return last_element
    else:
        return None
def is_empty(my_stack):
    # Verifica si la pila está vacía
    return lt.is_empty(my_stack)
def top(my_stack):
    # Devuelve el último elemento de la pila sin eliminarlo
    return lt.last_element(my_stack)
def size(my_stack):
    # Devuelve el tamaño de la pila
    return lt.size(my_stack)