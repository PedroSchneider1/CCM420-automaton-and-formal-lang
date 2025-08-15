estados = ["q1", "q2", "q3"]
inicial = "q1"
aceitacao = ["q2"]
alfabeto = ["0","1"]
transicao = {
    "q1":{"0":"q1",
        "1":"q2"},
    "q2":{"0":"q3",
        "1":"q2"},
    "q3":{"0":"q2",
        "1":"q2"}
}

palavra = list(input().split())
atual = inicial

for p in palavra:
    for c in p:
        if c not in alfabeto:
            atual = None
            break
        atual = transicao[atual][c]
    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")
