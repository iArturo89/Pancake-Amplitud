class Nodo:
    def __init__(self, estado, siguiente=None, movimiento=None):
        # Crea un nuevo Nodo con un estado dado, un Nodo siguiente opcional y un movimiento opcional.
        self.estado = estado
        self.siguiente = siguiente
        self.movimiento = movimiento

    def __repr__(self):
        # Retorna una representación en string del Nodo.
        return f"<Nodo {self.estado}>"

def obtener_hijos(nodo):
    # Crea y retorna una lista de los hijos de un Nodo dado.
    hijos = []
    for i in range(2, len(nodo.estado) + 1):
        # Itera a través del estado actual y crea un hijo para cada sublista de 2 o más elementos.
        volteado = nodo.estado[:i][::-1]  # Voltea la sublista.
        hijos.append(Nodo(volteado + nodo.estado[i:], siguiente=nodo, movimiento=(i, len(nodo.estado))))
        # Agrega el hijo a la lista de hijos.
    return hijos

def dfs(estado_inicial):
    # Realiza una búsqueda DFS en el árbol de estados, comenzando desde el estado inicial dado.
    nodo_estado = Nodo(estado_inicial)  # Crea un Nodo para el estado inicial.
    if estado_inicial == sorted(estado_inicial):
        # Si el estado inicial ya está ordenado, se retorna el Nodo con el estado inicial.
        return nodo_estado
    pila = [nodo_estado]  # Crea una pila con el Nodo inicial.
    visitados = {tuple(estado_inicial)}  # Crea un conjunto para mantener el registro de los estados visitados.
    while pila:
        # Mientras la pila no esté vacía, continúa la búsqueda.
        nodo = pila.pop()  # Selecciona el último Nodo de la pila.
        for hijo in obtener_hijos(nodo):
            # Para cada hijo del Nodo seleccionado, se realiza lo siguiente:
            if hijo.estado == sorted(estado_inicial):
                # Si el hijo tiene el estado final ordenado, se retorna el Nodo del hijo.
                return hijo
            if tuple(hijo.estado) not in visitados:
                # Si el estado del hijo no ha sido visitado anteriormente, se agrega a la pila y al conjunto de estados visitados.
                visitados.add(tuple(hijo.estado))
                pila.append(hijo)

def imprimir_solucion(nodo):
    # Imprime la solución a la consola, dada una Nodo con la solución.
    movimientos = []
    estados = []
    while nodo.siguiente is not None:
        # Recorre la solución desde el Nodo de la solución hasta el Nodo inicial, obteniendo los movimientos y los estados en el camino.
        movimientos.append(nodo.movimiento)
        estados.append(nodo.estado)
        nodo = nodo.siguiente
    movimientos.reverse()
    estados.reverse()
    for i in range(len(movimientos)-1):
        # Imprime cada movimiento y su resultado.
        print(f" {estados[i+1]}")
    print(estados[-1])

if __name__ == "__main__":
    # Código que se ejecutará si este archivo se ejecuta como un script independiente.
    estado_inicial = ['d', 'b', 'c', 'a']  # Modificación de la línea
    solucion = dfs(estado_inicial)
    imprimir_solucion(solucion)
