# ordem dos inputs
# 1 estados
# 2 estado inicial
# 3 aceitacao
# 4 alfabeto
# 5 transicoes
# 6 palavra

transicao = {}
estados = list(input().split())
inicial = input()
aceitacoes = list(input().split())
alfabeto = list(input().split())

for i in range(0, len(estados)):
    linhas_transicao = list(input().split())
    transicao.update({linhas_transicao[0]: {alfabeto[0]: linhas_transicao[1], alfabeto[1]: linhas_transicao[2]}})

palavras = list(input().split())
atual = inicial

for p in palavras:
    for c in p:
        if c not in alfabeto:
            atual = None
            break
        atual = transicao[atual][c]
    if atual in aceitacoes:
        print("aceita")
    else:
        print("rejeita")
    atual = inicial