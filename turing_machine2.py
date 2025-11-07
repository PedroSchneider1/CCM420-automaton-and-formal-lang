# input: palavra

estados = ['q1', 'q2', 'q3', 'q4', 'q5', 'q_accept', 'q_reject']
alfabeto = ['0']
alfabeto_fita = ['_', 'x', None]
transicoes = {
    ('q1', alfabeto[0]     ):   ('q2',       alfabeto_fita[0], 'R'),
    ('q1', alfabeto_fita[0]):   ('q_reject', alfabeto_fita[2], 'R'),
    ('q1', alfabeto_fita[1]):   ('q_reject', alfabeto_fita[2], 'R'),
    ('q2', alfabeto[0]     ):   ('q3',       alfabeto_fita[1], 'R'),
    ('q2', alfabeto_fita[0]):   ('q_accept', alfabeto_fita[2], 'R'),
    ('q2', alfabeto_fita[1]):   ('q2',       alfabeto_fita[2], 'R'),
    ('q3', alfabeto[0]     ):   ('q4',       alfabeto_fita[2], 'R'),
    ('q3', alfabeto_fita[1]):   ('q3',       alfabeto_fita[2], 'R'),
    ('q3', alfabeto_fita[0]):   ('q5',       alfabeto_fita[2], 'L'),
    ('q4', alfabeto[0]     ):   ('q3',       alfabeto_fita[1], 'R'),
    ('q4', alfabeto_fita[1]):   ('q4',       alfabeto_fita[2], 'R'),
    ('q4', alfabeto_fita[0]):   ('q_reject', alfabeto_fita[2], 'R'),
    ('q5', alfabeto[0]     ):   ('q5',       alfabeto_fita[2], 'L'),
    ('q5', alfabeto_fita[1]):   ('q5',       alfabeto_fita[2], 'L'),
    ('q5', alfabeto_fita[0]):   ('q2',       alfabeto_fita[2], 'R')
}
inicial = 'q1'

def processar_palavra(palavra):
    fita = list(palavra) + [alfabeto_fita[0]]  # adiciona símbolo de branco no fim
    cabecote = 0
    estado_atual = inicial
    impressao_fita = fita.copy()

    while True:
        impressao_fita = fita[:cabecote].copy() + [estado_atual] + fita[cabecote:].copy()
        print(f'{" ".join(impressao_fita)}')
        simbolo_atual = fita[cabecote]

        chave = (estado_atual, simbolo_atual)

        if chave not in transicoes:
            break

        novo_estado, simbolo_escrito, direcao = transicoes[chave]
        if simbolo_escrito is not None:
            fita[cabecote] = simbolo_escrito
        estado_atual = novo_estado
        cabecote += 1 if direcao == 'R' else -1

        if novo_estado in ['q_accept', 'q_reject']:
            return novo_estado

# Exemplo de uso
palavra = input().strip()
estado_final = processar_palavra(palavra)
if estado_final == 'q_accept':
    print("aceita")
else:
    print("rejeita")

