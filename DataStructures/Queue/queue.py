def new_queue():
    """
    Crea una nueva cola vacía.
    """
    return q.new_queue()
def enqueue(queue, element):
    """
    Agrega un elemento al final de la cola.
    """
    return q.enqueue(queue, element)
def dequeue(queue):
    """
    Elimina y retorna el primer elemento de la cola.
    """
    return q.dequeue(queue)
def peek(queue):
    """
    Retorna el primer elemento de la cola sin eliminarlo.
    """
    return q.peek(queue)
def is_empty(queue):
    """
    Verifica si la cola está vacía.
    """
    return q.is_empty(queue)
def size(queue):
    """
    Retorna el tamaño de la cola.
    """
    return q.size(queue)