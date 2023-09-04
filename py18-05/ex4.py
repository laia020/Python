def numero (n1,n2,n3,n4) :
    lista = [n1,n2,n3,n4]
    lista.sort(reverse = True)
    print(lista)

print("Digite 4 números reais")
nmr1 = input()
nmr2 = input()
nmr3 = input()
nmr4 = input()
numero(nmr1,nmr2,nmr3,nmr4)