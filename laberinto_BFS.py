from collections import deque

# Representación del laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posición de inicio y salida
start = (0, 1)  # Coordenadas (fila, columna) de inicio
end = (3, 4)    # Coordenadas (fila, columna) de salida

# Función para verificar si una posición es válida
def is_valid(maze, visited, position):
    row, col = position
    return (0 <= row < len(maze) and
            0 <= col < len(maze[0]) and
            maze[row][col] == 0 and
            not visited[row][col])

# Función para realizar BFS
def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])  # Cola para BFS
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    parent = {start: None}  # Para reconstruir el camino

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

    while queue:
        current = queue.popleft()

        if current == end:
            break

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            next_position = (next_row, next_col)

            if is_valid(maze, visited, next_position):
                visited[next_row][next_col] = True
                queue.append(next_position)
                parent[next_position] = current

    # Reconstruir el camino
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()  # Invertir el camino para tenerlo desde el inicio hasta el final

    return path if path[0] == start else None

# Ejecutar BFS y mostrar el camino encontrado
path = bfs(maze, start, end)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró ningún camino.")
