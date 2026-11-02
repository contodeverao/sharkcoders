# Jogo da Adivinhação em Python

# Mensagem inicial
print("Jogo da Adivinhação")
print("Estou a pensar num número entre 1 e 10...")

# Número secreto definido pelo programador
numero_secreto = 7

# O jogador tenta adivinhar
palpite = int(input("Qual número você acha que é? "))

# Verifica se acertou, se passou ou se ficou abaixo
if palpite == numero_secreto:
    print("Acertou! Muito bem!")
elif palpite > numero_secreto:
    print("Muito alto! O número secreto é menor.")
else:
    print("Muito baixo! O número secreto é maior.")

# Mensagem final
print("Fim do jogo.")
