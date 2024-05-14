import itertools

# Função para calcular a distância total de um determinado percurso
def calcular_distancia_total(percurso, matriz_distancias):
    distancia_total = 0
    num_cidades = len(percurso)
    for i in range(num_cidades - 1):
        distancia_total += matriz_distancias[percurso[i]][percurso[i + 1]]
    distancia_total += matriz_distancias[percurso[-1]][percurso[0]]  # Retorna à cidade inicial
    return distancia_total

# Função para encontrar o percurso ótimo
def caixeiro_viajante(matriz_distancias):
    num_cidades = len(matriz_distancias)
    cidades = list(range(num_cidades))
    menor_distancia = float('inf')
    melhor_percurso = []

    for percurso in itertools.permutations(cidades):
        distancia = calcular_distancia_total(percurso, matriz_distancias)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_percurso = percurso

    return melhor_percurso, menor_distancia

# Exemplo de uso
if __name__ == "__main__":
    # Matriz de distâncias entre as cidades (exemplo)
    matriz_distancias = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    percurso_otimo, distancia_otima = caixeiro_viajante(matriz_distancias)
    print(f"Melhor percurso: {percurso_otimo}")
    print(f"Distância total: {distancia_otima} unidades")

