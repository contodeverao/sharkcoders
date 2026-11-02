# Programa: Mini Batalha Ninja

print("=== Batalha Ninja ===")

print("Escolha o seu personagem:")
print("1 - Naruto")
print("2 - Sasuke")
print("3 - Sakura")

escolha = int(input("Digite o número do personagem: "))

print("\nVocê encontrou um inimigo misterioso!")

# Condições para definir o resultado da batalha
if escolha == 1:
    print("Naruto usa o Rasengan e derrota o inimigo!")
elif escolha == 2:
    print("Sasuke ativa o Sharingan e vence a batalha!")
elif escolha == 3:
    print("Sakura usa sua super força e derrota o inimigo!")
else:
    print("Opção inválida. O inimigo aproveitou a sua distração e você perdeu!")

print("\nFim da batalha.")


