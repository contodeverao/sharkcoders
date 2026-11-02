# Programa: Criando um perfil simples

print("Bem-vindo ao Criador de Perfis!")

# Guardar informações em variáveis
nome = input("Qual é o seu nome? ")
idade = input("Quantos anos você tem? ")
cidade = input("Em que cidade você mora? ")
hobby = input("Qual é o seu hobby favorito? ")
cor = input("Qual é a sua cor preferida? ")

# Mostrar um resumo com base nas respostas
print("\n--- Perfil Criado ---")
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Cidade:", cidade)
print("Hobby favorito:", hobby)
print("Cor preferida:", cor)

# Mensagem final personalizada
print("\nMuito bem,", nome + "!")
print("Com apenas", idade, "anos, já sabemos que você gosta de", hobby,
      "e que a cor", cor, "é a sua favorita.")
print("Continue sempre a aprender e a explorar novas ideias!")
