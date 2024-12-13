import sys

def main():
    input = sys.stdin.read
    dados = input().strip().split("\n")
    
    cidade_num = 1
    i = 0

    while i < len(dados):
        n = int(dados[i])
        i += 1

        if n == 0:
            break

        cidades = {}
        total_populacao = 0
        total_consumo = 0

        for _ in range(n):
            moradores, consumo = map(int, dados[i].split())
            i += 1

            consumo_por_pessoa = consumo // moradores

            if consumo_por_pessoa in cidades:
                cidades[consumo_por_pessoa].append(moradores)
            else:
                cidades[consumo_por_pessoa] = [moradores]

            total_populacao += moradores
            total_consumo += consumo

        print(f"Cidade# {cidade_num}:")

        consumo_ordenado = sorted(cidades.items())
        resultado = []
        for consumo, pops in consumo_ordenado:
            for pop in pops:
                resultado.append(f"{pop}-{consumo}")
        
        print(" ".join(resultado))

        media_consumo = total_consumo / total_populacao
        print(f"Consumo medio: {media_consumo:.2f} m3.")
        
        cidade_num += 1

        if i < len(dados) and int(dados[i]) != 0:
            print("")

if __name__ == "__main__":
    main()
