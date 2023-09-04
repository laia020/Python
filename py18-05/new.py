'''def frase1() :
    print("Hello World")

def frase2() :
    return "Hello Word"
frase1()
texto = frase2()
print(texto) '''

'''def soma(n1,n2) :
    result = n1 + n2
    return result

print("Digite 2 números inteiros")
num1 = int(input())
num2 = int(input())
resultado = soma(num1,num2)
print(f"A soma é: {resultado}")'''

def situacao(estado) :
    if estado.lower() == "solteiro" :
        print("você é solteiro")
    else :
        print("Você é casado")

print("Digite seu estado civil")
ecivil = input()
situacao(ecivil)


