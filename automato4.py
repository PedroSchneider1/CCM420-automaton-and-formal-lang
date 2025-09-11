# ordem dos inputs
# 1 estados
# 2 alfabeto
# 3 estado inicial
# 4 aceitacao
# 5 transicoes
# 6 palavra

"""
q1 q2 q3 q4
0 1
q1
q4
q1 q1 q1,q2 vazio
q2 q3 vazio q3
q3 vazio q4 vazio
q4 q4 q4 vazio
010110
"""

# Entrada
estados = list(input().split())
alfabeto = list(input().split())
inicial = input().strip()
aceitacoes = input().split()

transicao = {}
for i in range(len(estados)):
    linhas_transicao = list(input().split())
    estado_i = linhas_transicao[0]
    
    transicao[estado_i] = {}
    transicao[estado_i][alfabeto[0]] = [] if linhas_transicao[1] == "vazio" else linhas_transicao[1].split(",")
    transicao[estado_i][alfabeto[1]] = [] if linhas_transicao[2] == "vazio" else linhas_transicao[2].split(",")
    transicao[estado_i]["epsilon"] = [] if linhas_transicao[3] == "vazio" else linhas_transicao[3].split(",")

palavra = input().strip()

# Função para calcular fecho-epsilon (mantendo lista com duplicatas)
def fecho_epsilon(estados_atual):
    resultado = estados_atual[:]  # copia lista
    pilha = estados_atual[:]      # estados a processar
    
    while pilha:
        estado = pilha.pop()
        for prox_estado in transicao[estado]["epsilon"]:
            resultado.append(prox_estado)   # permite duplicatas
            pilha.append(prox_estado)
    
    return sorted(resultado)

# Estado inicial
atual = fecho_epsilon([inicial])
print(atual)

for c in palavra:
    if c not in alfabeto:
        atual = []
        break

    print(c)  # imprime símbolo
    
    # Calcular próximo conjunto de estados
    proximo = []
    for estado in atual:
        for destino in transicao[estado].get(c, []):
            proximo.append(destino)

    # Aplicar fecho-epsilon ao próximo conjunto
    atual = fecho_epsilon(proximo)
    print(atual)

# Verificar aceitação
aceito = any(estado in aceitacoes for estado in atual)

if aceito:
    print("aceita")
else:
    print("rejeita")
