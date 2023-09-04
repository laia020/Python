def parImp(numero) :
    if numero % 2 == 0 :
        print("número par")
    else:
        print("número Impar")
nmr = int
while nmr != 0 :
    print("Digite um número inteiro")
    nmr = int(input())
    parImp(nmr)
print("acabou")
    