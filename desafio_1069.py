n = int(input())
for _ in range(n):
    linha = input()
    linha = linha.replace('.', '')
    pilha = []
    diamantes = 0
    for char in linha:
        if char == '<':
            pilha.append('<')
        elif char == '>' and pilha:
            pilha.pop()
            diamantes += 1
    print(diamantes)