# Pancake-Amplitud
este codigo tiliza el algoritmo BFS para resolver el problema del ordenamiento de una lista. 
El objetivo del problema es ordenar una lista de elementos en orden ascendente, 
utilizando solo una operación de volteo que invierte el orden de los elementos en una sublista de la lista.

El script define una clase Nodo que representa un estado en el árbol de búsqueda BFS. 
Cada Nodo tiene un estado (una lista de elementos),
un puntero a un Nodo siguiente en el árbol y un movimiento (una tupla que indica el índice inicial y final de la sublista volteada para llegar a ese estado).

La función obtener_hijos(nodo) recibe un Nodo y devuelve una lista de todos sus hijos posibles.
Cada hijo es creado volteando una sublista de 2 o más elementos del estado del padre.

La función bfs(estado_inicial) recibe el estado inicial de la lista desordenada y realiza una búsqueda BFS en el árbol de estados para encontrar el estado final ordenado.
La función devuelve el Nodo correspondiente al estado final.

La función imprimir_solucion(nodo) recibe el Nodo de la solución y muestra en la consola el camino desde el estado inicial hasta el estado final.
El camino se construye retrocediendo desde el Nodo final hasta el Nodo inicial y registrando los movimientos realizados en cada paso.

Si se ejecuta el archivo como un script independiente, se define un estado inicial y se llama a la función bfs y imprimir_solucion para mostrar la solución en la consola.


Para utilizar el script, se puede modificar el estado inicial en la línea estado_inicial = ['d', 'b', 'c', 'a'] antes de ejecutar el archivo.
