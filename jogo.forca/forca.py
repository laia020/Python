import random
print("Escolha:\npedra\npapel\ntesoura")
jogador = input()
sorteio = random.randint(1,3)
if sorteio == 1:
    pc = "pedra"
else:
    if sorteio == 2:
        pc = "papel"
    else:
        pc = "tesoura"

#testando empate
if jogador == pc :
    print(f"O jogo deu empate\nJogador:{jogador}\nPC:{pc}")
else :
    if jogador == "papel" and pc == "tesoura" :
       print(f"Você perdeu\nJogador:{jogador}\nPC:{pc}")
    if jogador == "papel" and pc == "pedra" :
       print(f"Você venceu\nJogador:{jogador}\nPC:{pc}")
    if jogador == "pedra" and pc == "papel" :
       print(f"Você perdeu\nJogador:{jogador}\nPC:{pc}")
    if jogador == "pedra" and pc == "tesoura" :
       print(f"Você venceu\nJogador:{jogador}\nPC:{pc}")
    if jogador == "tesoura" and pc == "pedra" :
       print(f"Você perdeu\nJogador:{jogador}\nPC:{pc}")
    if jogador == "tesoura" and pc == "papel" :
       print(f"Você venceu\nJogador:{jogador}\nPC:{pc}")