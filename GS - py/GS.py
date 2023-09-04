import re

print ("Bem vindo a FEEDING AI")

#1º laço Para o nome
while True:
    nome = input("\nDigite seu nome para se cadastrar (não pode conter números): ")

    try:
        if re.search("\d", nome):
            raise ValueError("O nome não pode conter números.")
        break  # Sai do loop
    except ValueError:
        print("\nNão foi possível realizar o cadastro. O nome não pode conter números.")
        print("Por favor, digite novamente.")

#2º laço para a senha 
while True:
    senha = input("\nEscolha uma senha de 5 dígitos númericos, mais 1 letra maiúscula (no inicio ou ao final dos dígitos): ")

    if len(senha) != 6:
        print("\nSenha inválida. A senha deve conter 5 números e 1 letra maiúscula.")
        print("Por favor, digite novamente.")
        continue

    if not re.search(r"\d{5}", senha):
        print("Senha inválida. A senha deve conter 5 números e 1 letra maiúscula.")
        print("Por favor, digite novamente.")
        continue

    if not re.search(r"[A-Z]", senha):
        print("Senha inválida. A senha deve conter 5 números e 1 letra maiúscula.")
        print("Por favor, digite novamente.")
        continue

    break  # Senha válida, sai do loop



#loop para menu menu
while True:
    print("\nSelecione uma opção:")
    print("1. Quero fazer uma doação")
    print("2. Quero conhecer mais sobre a empresa")
    print("3. Sair")

    opcao = input("\nDigite o número da opção desejada: ")


    if opcao == "1":
        print("\nOpção selecionada: Quero fazer uma doação")
        print("Deseja fazer sua doação como Pessoa Fisíca ou Jurídica ?")
        print("1. Jurídico")
        print("2. Pessoa Fisíca")

        cadastro = input("\nDigite o númnero da opção desejada: ")

        if cadastro == "2":
            nome_doador = input("\nDigite o nome do Doador: ")

            alimentos = []

            for i in range(4):
                alimento = input("Digite o {}º alimento: ".format(i+1))
                alimentos.append(alimento)

            estado = input("\nDigite o estado em qual deseja fazer a doação: ")

            while True:
                cpf = input("\nDigite o CPF do responsável (11 dígitos, apenas dígitos): ")
                
                cpf = ''.join(filter(str.isdigit, cpf))
                
                if len(cpf) != 11:
                    print("CPF inválido! O CPF deve conter 11 dígitos.")
                else:
                    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                    print("CPF cadastrado com sucesso:", cpf_formatado)
                    break

        elif cadastro == "1":
            empresa_doadora = input("Digite o nome da empresa reponsável: ")   

            alimentos = []

            for i in range(4):
                alimento = input("Digite o {}º alimento: ".format(i+1))
                alimentos.append(alimento)

            estado = input("Digite o estado em qual deseja fazer a doação: ")

            print()
            while True:
                cnpj = input("Digite o CNPJ da empresa responsável(14 dígitos, apenas dígitos): ")
                
                cnpj = ''.join(filter(str.isdigit, cnpj))
                
                if len(cnpj) != 14:
                    print("CNPJ inválido! O CNPJ deve conter 14 dígitos.")
                else:
                    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
                    print("CNPJ cadastrado com sucesso:", cnpj_formatado)
                    break   

        print("\nJuntamente com os alimentos que deseja doar, leve seus dados cadastrados para uma de nossas centrais localizadas em seu estado")    
        if cadastro == "2":
            print(f"\nO nome do doader é: {nome_doador}")
            print(f"Seu CPF cadastrado é: {cpf_formatado}") 
            print(f"Seu estado cadastrado é: {estado}")
            print(f"Os alimentos adicionados são: {alimentos}")
        elif cadastro == "1":
            print(f"\nO nome da empresa doadora é: {empresa_doadora}")
            print(f"Seu CNPJ cadastrado é: {cnpj_formatado}")
            print(f"Seu estado cadastrado é: {estado}")
            print(f"Os alimentos adicionados são: {alimentos}")


                   


    elif opcao == "2":
        print("\nOpção selecionada: Conhecer mais sobre o app")
        print("\nCom a nossa solução FEEDING AI, usando IA generativa, encontramos uma forma de geração de receitas personalizadas para indivíduos em situação de insegurança alimetar")
        print("\nAcreditamos que qualquer pessoa merece ter acesso a alimentos nutritivos e suficientes. Com empatia e inovação, estamos construindo pontes para um futuro onde ninguém precise sentir a dor da fome")
        # Aqui você pode adicionar mais informações sobre o aplicativo

    elif opcao == "3":
        print("Saindo do programa...")
        break  # Sai do loop e encerra o programa

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


    continuar = input("\nDeseja voltar ao menu? (s/n) ")

    # Caso não queira, o codigo para
    if continuar.lower() != 's':
        break

    print("\n")  # Linha em branco para separar as opções

print("Obrigado por utilizar  FEEDING AI!")