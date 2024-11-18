import math
 
# Função para calcular a distância Manhattan
def distancia_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
 
# Função para verificar se a posição é válida (dentro do labirinto e sem obstáculos)
def posicao_valida(labirinto, p):
    x, y = p
    if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] != '1':
        return True
    return False
 
# Função para obter os vizinhos válidos
def obter_vizinhos(labirinto, p):
    x, y = p
    vizinhos = [
        (x-1, y), (x+1, y), (x, y-1), (x, y+1)  # cima, baixo, esquerda, direita
    ]
    return [v for v in vizinhos if posicao_valida(labirinto, v)]
 
# Função de Hill Climbing
def hill_climbing(labirinto, inicio, saida):
    atual = inicio
    caminho = [atual]
 
    while atual != saida:
        vizinhos = obter_vizinhos(labirinto, atual)
        if not vizinhos:
            break  # Se não houver vizinhos válidos, pare
 
        # Escolhe o vizinho com a menor distância até a saída
        melhor_vizinho = min(vizinhos, key=lambda v: distancia_manhattan(v, saida))
        # Se o movimento não melhora a posição (impasse), pare
        if distancia_manhattan(melhor_vizinho, saida) >= distancia_manhattan(atual, saida):
            break
        atual = melhor_vizinho
        caminho.append(atual)
 
    return caminho
 
# Função para rodar as simulações
def simular_labirinto(labirinto, inicio, saida):
    caminho = hill_climbing(labirinto, inicio, saida)
    if saida in caminho:
        print(f"Sucesso! Caminho encontrado: {caminho}")
    else:
        print(f"Falha! Não foi possível encontrar um caminho até a saída.")
 
# Simulação 1: Labirinto Simples com Caminho Claro
labirinto_1 = [
    ['S', '0', '0'],
    ['1', '1', '0'],
    ['0', '0', 'E']
]
simular_labirinto(labirinto_1, (0, 0), (2, 2))
 
# Simulação 2: Labirinto com Obstáculos e Caminho Complicado
labirinto_2 = [
    ['S', '0', '1', '1', '0', '0'],
    ['0', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '0'],
    ['1', '1', '1', '0', '0', 'E']
]
simular_labirinto(labirinto_2, (0, 0), (3, 5))
 
# Simulação 3: Labirinto com Entradas e Saídas Múltiplas
labirinto_3 = [
    ['S', '0', '1', '0', '0', '0'],
    ['1', '0', '1', '1', '0', '0'],
    ['0', '0', '0', '1', '0', 'E'],
    ['1', '1', '0', '0', '1', '0'],
    ['0', '0', '0', '0', '0', '0']
]
simular_labirinto(labirinto_3, (0, 1), (2, 5))
 
# Simulação 4: Labirinto sem Solução
labirinto_4 = [
    ['S', '1', '1'],
    ['1', '0', '1'],
    ['1', '0', 'E']
]
simular_labirinto(labirinto_4, (0, 0), (2, 2))
 
# Simulação 5: Labirinto Grande com Obstáculos Aleatórios
labirinto_5 = [
    ['S', '0', '0', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '1', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '0', '0', '0', '0', '1', '0', '0'],
    ['0', '1', '0']]
simular_labirinto(labirinto_5, (0, 0), (2, 2))