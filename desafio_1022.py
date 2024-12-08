from math import gcd

def simplificar(numerador, denominador):
    divisor = gcd(numerador, denominador)
    return numerador // divisor, denominador // divisor

def processar_casos(casos):
    resultados = []
    for caso in casos:
        n1, barra1, d1, operador, n2, barra2, d2 = caso.split()
        n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
        
        if operador == '+':
            numerador = n1 * d2 + n2 * d1
            denominador = d1 * d2
        elif operador == '-':
            numerador = n1 * d2 - n2 * d1
            denominador = d1 * d2
        elif operador == '*':
            numerador = n1 * n2
            denominador = d1 * d2
        elif operador == '/':
            numerador = n1 * d2
            denominador = d1 * n2
        
        numerador_simp, denominador_simp = simplificar(numerador, denominador)
        
        resultado = f"{numerador}/{denominador} = {numerador_simp}/{denominador_simp}"
        resultados.append(resultado)
    
    return resultados

n = int(input())
casos = [input().strip() for _ in range(n)]

resultados = processar_casos(casos)
print("\n".join(resultados))