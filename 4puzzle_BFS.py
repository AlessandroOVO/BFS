from biblioteca1 import Lista, Pila, Cola, Objeto
from collections import deque


def bfs(estado_inicial, estado_objetivo):
    # Cola para los estados a explorar
    cola = deque([(estado_inicial, "")])#Cola que inicialmente contiene una tupla con el estado inicial y una cadena vacia que representara el camino tomado
    visitado = set() #inicializa un conjunto para rastrear los estados que ya se han explorado
    visitado.add(tuple(map(tuple, estado_inicial)))#convierte el estado inicial en una tupla de tuplas

    while cola:#Se ejecuta mientras haya estados en la cola
        estado, camino = cola.popleft()#Extrae el primer elemento de la cola que es el estado actual y el camino tomado

        # Verifica si hemos llegado al estado objetivo
        if estado == estado_objetivo:
            return camino

        # Encuentra la posición del espacio vacío (0)
        zero_pos = [(i, j) for i in range(2) for j in range(2) if estado[i][j] == 0][0] #Encontrar la posicion del 0
        x, y = zero_pos #Asigna la posicion del 0 a x,y

        # Movimientos posibles (arriba, abajo, izquierda, derecha)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)] #Lista de movimientos 
        for dx, dy in direcciones:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < 2 and 0 <= new_y < 2: #Verifica si la nueva posicion esta dentro de los limites de la cuadricula
                # Crea un nuevo estado intercambiando el 0
                new_estado = [row[:] for row in estado]  # Copia del estado
                new_estado[x][y], new_estado[new_x][new_y] = new_estado[new_x][new_y], new_estado[x][y]

                if tuple(map(tuple, new_estado)) not in visitado:
                    visitado.add(tuple(map(tuple, new_estado)))
                    cola.append((new_estado, camino + f"{(new_x, new_y)} "))

    return None  # No se encontró solución

# Estado inicial y estado objetivo
initial = [[1, 2], [0, 3]]
goal = [[1, 2], [3, 0]]

solution = bfs(initial, goal)
if solution:
    print("Solución encontrada con los movimientos:", solution)
else:
    print("No se encontró solución.")

