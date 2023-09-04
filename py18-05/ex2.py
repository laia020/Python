import math
def raiz(n1) :
    result = math.sqrt(n1)
    return result

print("Digite um número inteiro")
num1 = int(input())
resultado = raiz(num1)
print(f"A raiz quadrada é: {resultado}")