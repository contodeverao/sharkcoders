# Programa: Teste Ninja

print("=== Bem-vindo ao Teste Ninja ===")

# Coletar informações
nome = input("Qual é o seu nome ninja? ")
idade = int(input("Quantos anos você tem? "))
chakra = int(input("Quanto de chakra você tem? (0 a 100) "))

print("\n--- Resultado do Teste ---")

# Condições com operadores relacionais
if idade >= 18 and chakra >= 70:
    print(nome, "é um Jounin! Um verdadeiro mestre ninja.")
elif idade >= 16 and chakra >= 50:
    print(nome, "é um Chuunin! Já tem bastante experiência.")
elif idade >= 12 and chakra >= 30:
    print(nome, "é um Genin! Está pronto para começar as missões.")
else:
    print(nome, "ainda é um Estudante da Academia Ninja. Continue treinando!")

print("\nFim do teste. Continue a evoluir, ninja", nome + "!")
