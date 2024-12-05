from collections import defaultdict
assassinatos = defaultdict(int)
vitimas = set()
x = []
while True:
    try:
        entrada = input().strip()
        if entrada:
            x.append(entrada.split())
    except EOFError:
        break
for assassino, vítima in x:
    assassinatos[assassino] += 1
    vitimas.add(vítima)
resultado = [
    (nome, contador) for nome, contador in assassinatos.items() if nome not in vitimas
]
resultado.sort(key=lambda item: item[0])
print("HALL OF MURDERERS")
for nome, contador in resultado:
    print(f"{nome} {contador}")
