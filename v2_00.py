import heapq

TAMAÑO_MATRIZ = 20
COSTO_POR_DEFECTO = 1

matriz_madre = [
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [1, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 0, 2],
    [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
    [2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1],
]


class Nodo:
    def __init__(self, x, y, costo):
        self.x = x
        self.y = y
        self.costo = costo
        self.g = float('inf')  
        self.h = 0  
        self.f = float('inf')  
        self.padre = None

    def __lt__(self, otro):
        return self.f < otro.f

def heuristica(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def a_estrella(matriz, inicio, fin):
    lista_abierta = []
    heapq.heappush(lista_abierta, inicio)
    inicio.g = 0
    inicio.f = heuristica(inicio, fin)

    while lista_abierta:
        actual = heapq.heappop(lista_abierta)

        if actual == fin:
            return reconstruir_camino(actual)

        for vecino in obtener_vecinos(matriz, actual):
            g_tentativo = actual.g + vecino.costo

            if g_tentativo < vecino.g:
                vecino.padre = actual
                vecino.g = g_tentativo
                vecino.h = heuristica(vecino, fin)
                vecino.f = vecino.g + vecino.h
                if vecino not in lista_abierta:
                    heapq.heappush(lista_abierta, vecino)

    return None

def obtener_vecinos(matriz, nodo):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vecinos = []

    for dx, dy in direcciones:
        x, y = nodo.x + dx, nodo.y + dy
        if 0 <= x < TAMAÑO_MATRIZ and 0 <= y < TAMAÑO_MATRIZ:
            vecinos.append(matriz[x][y])

    return vecinos

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append((nodo.x, nodo.y))
        nodo = nodo.padre
    return camino[::-1]

def crear_matriz(costos):
    return [[Nodo(x, y, costos[x][y]) for y in range(TAMAÑO_MATRIZ)] for x in range(TAMAÑO_MATRIZ)]

def dibujar_matriz(matriz, camino, inicio, fin):
    for i in range(TAMAÑO_MATRIZ):
        for j in range(TAMAÑO_MATRIZ):
            if (i, j) in camino:
                simbolo = '*'
            elif (i, j) == (inicio.x, inicio.y):
                simbolo = 'I'
            elif (i, j) == (fin.x, fin.y):
                simbolo = 'F'
            else:
                simbolo = str(matriz[i][j].costo)
            print(simbolo, end=' ')
        print()

def obtener_entrada_usuario():
    obstáculos = []
    for i in range(3):
        while True:
            try:
                x = int(input(f"Ingrese la coordenada x del obstáculo tipo {i+1} (0-{TAMAÑO_MATRIZ-1}): "))
                y = int(input(f"Ingrese la coordenada y del obstáculo tipo {i+1} (0-{TAMAÑO_MATRIZ-1}): "))
                costo = int(input(f"Ingrese el costo del obstáculo tipo {i+1}: "))
                if 0 <= x < TAMAÑO_MATRIZ and 0 <= y < TAMAÑO_MATRIZ:
                    obstáculos.append((x, y, costo))
                    break
                else:
                    print("Coordenadas fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
    return obstáculos

def main():
    matriz = crear_matriz(matriz_madre)
    
    while True:
        try:
            inicio_x = int(input("Ingrese la coordenada x del punto de inicio (0-19): "))
            inicio_y = int(input("Ingrese la coordenada y del punto de inicio (0-19): "))
            fin_x = int(input("Ingrese la coordenada x del punto final (0-19): "))
            fin_y = int(input("Ingrese la coordenada y del punto final (0-19): "))
            if 0 <= inicio_x < TAMAÑO_MATRIZ and 0 <= inicio_y < TAMAÑO_MATRIZ and 0 <= fin_x < TAMAÑO_MATRIZ and 0 <= fin_y < TAMAÑO_MATRIZ:
                break
            else:
                print("Coordenadas fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

    obstáculos = obtener_entrada_usuario()
    for x, y, costo in obstáculos:
        matriz[x][y].costo = costo

    inicio = matriz[inicio_x][inicio_y]
    inicio.costo = COSTO_POR_DEFECTO
    fin = matriz[fin_x][fin_y]
    fin.costo = COSTO_POR_DEFECTO

    camino = a_estrella(matriz, inicio, fin)

    if camino:
        print("Camino encontrado:")
        dibujar_matriz(matriz, camino, inicio, fin)
    else:
        print("No se encontró un camino.")

if __name__ == "__main__":
    main()
