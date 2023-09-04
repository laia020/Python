#função para definir o primeiro número
def multi(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    ml1 = n1 * 10
    ml2 = n2 * 9
    ml3 = n3 * 8
    ml4 = n4 * 7
    ml5 = n5 * 6
    ml6 = n6 * 5
    ml7 = n7 * 4
    ml8 = n8 * 3
    ml9 = n9 * 2
    
    soma = ml1 + ml2 + ml3 + ml4 + ml5 + ml6 + ml7 + ml8 + ml9

    divi = soma%11 
  
    if divi < 2:
        pdi = 0
    else:
        pdi = 11 - divi

    return pdi   

#função para definir o segundo número
def multi2(n1,n2,n3,n4,n5,n6,n7,n8,n9,digito1):
    ml1 = n1 * 11
    ml2 = n2 * 10
    ml3 = n3 * 9
    ml4 = n4 * 8
    ml5 = n5 * 7
    ml6 = n6 * 6
    ml7 = n7 * 5
    ml8 = n8 * 4
    ml9 = n9 * 3
    ml10 = digito1 * 2

    soma = ml1 + ml2 + ml3 + ml4 + ml5 + ml6 + ml7 + ml8 + ml9 + ml10
    
    divi = soma % 11
    
    if divi < 2:
        sdi = 0
    else:
        sdi = 11 - divi

    return sdi

#usuário digita o cpf e ele é tranformado em variável
print("Digite seu CPF")

cpf = str(input())
n1 = int(cpf[0])
n2 = int(cpf[1])
n3 = int(cpf[2])
n4 = int(cpf[3])
n5 = int(cpf[4])
n6 = int(cpf[5])
n7 = int(cpf[6])
n8 = int(cpf[7])
n9 = int(cpf[8])

#numeros finais são transformados em variável
digito1 = multi(n1,n2,n3,n4,n5,n6,n7,n8,n9)
digito2 = multi2(n1,n2,n3,n4,n5,n6,n7,n8,n9, digito1)

#se os dois numeros que foram resultados nas funções estiverem certos o usuário é notificado
if int(cpf[9]) == digito1 and digito2 == int(cpf[10]):
    print("O RG está certo!")
else:
    print("O RG está errado!")