import math
 
# Definindo o labirinto
labirinto = [
   ['S', '0', '1', '0', '0', '0'],
   ['0', '1', '0', '1', '0', '0'],
   ['0', '1', '0', '1', '0', '0'],
   ['0', '0', '0', '1', '1', 'E']
]
 
# Tamanho do labirinto
linhas = len(labirinto)
colunas = len(labirinto[0])
 
# Posições de início (S) e fim (E)
inicio = (0, 0)
saida = (3, 5)
 
# Função para calcular a distância Manhattan
def distancia_manhattan(p1, p2):
   return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
 
# Função para verificar se a posição é válida (dentro do labirinto e sem obstáculos)
def posicao_valida(p):
   x, y = p
   if 0 <= x < linhas and 0 <= y < colunas and labirinto[x][y] != '1':
       return True
   return False
 
# Função para obter os vizinhos válidos
def obter_vizinhos(p):
   x, y = p
   vizinhos = [
       (x-1, y), (x+1, y), (x, y-1), (x, y+1)  # cima, baixo, esquerda, direita
   ]
   return [v for v in vizinhos if posicao_valida(v)]
 
# Função de Hill Climbing
def hill_climbing(inicio, saida):
   atual = inicio
   caminho = [atual]
 
   while atual != saida:
       vizinhos = obter_vizinhos(atual)
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
 
# Testando o agente
caminho = hill_climbing(inicio, saida)
print("Caminho percorrido pelo agente:", caminho)