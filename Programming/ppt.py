import random

vitoria = { "pedra": "papel",
            "papel": "tesoura",
            "tesoura": "pedra",}

def lanceComputador():
    lance = random.randint(1,3)
    if lance == 1:
        return "pedra"
    if lance == 2:
        return "papel"
    if lance == 3:
        return "tesoura"

jogada = input("Qual a sua jogada? (pedra/papel/tesoura) ou Sair")

lance = lanceComputador()

if lance == vitoria[jogada]:
    print("Ganhou o computador")
elif lance == jogada:
    print("Empate")
else:
    print("Ganhou o jogador")