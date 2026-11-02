# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 04 — Exercício 2: Máquina de Sumos
# ============================================================
# Conceitos: operador in, listas, join()
# ============================================================


# ------------------------------------------------------------
# CONCEITO — Operador in
# ------------------------------------------------------------
# O "in" verifica se um valor existe dentro de uma lista
# ou de uma string. Devolve True ou False.
#
#   "a" in "banana"         → True
#   "z" in "banana"         → False
#   5   in [1, 3, 5, 7]    → True
#   10  in [1, 3, 5, 7]    → False
#   "laranja" in opcoes     → True (se estiver na lista)
#
# Sem "in" precisaríamos de escrever:
#   if escolha == "maça" or escolha == "laranja" or ...
# Com "in" fica muito mais simples e fácil de manter!
#
# join() junta os elementos de uma lista numa string:
#   ", ".join(["a", "b", "c"]) → "a, b, c"
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────

print("=== Máquina de Sumos ===")

opcoes_disponiveis = ["maça", "laranja", "manga", "morango"]

print("Sumos disponíveis:", ", ".join(opcoes_disponiveis))
escolha = input("Qual sumo queres? ").strip().lower()

if escolha in opcoes_disponiveis:
    print(f"🥤 Aqui está o teu sumo de {escolha}! Bom proveito!")
else:
    print(f"❌ Desculpa, não temos sumo de {escolha}.")
    print("   Escolhe um dos seguintes:", ", ".join(opcoes_disponiveis))


# ============================================================
# EXTRA 1 — Máquina com duas categorias
# ============================================================
# A máquina agora tem sumos E águas.
# Pede ao utilizador o que quer beber e a categoria.
# Verifica com "in" se existe na categoria correcta.
#
# sumos = ["maça", "laranja", "manga", "morango"]
# aguas = ["com gas", "sem gas", "com limao"]
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Sumos e Águas ===")
# sumos = ["maça", "laranja", "manga", "morango"]
# aguas = ["com gas", "sem gas", "com limao"]
#
# categoria = input("Queres sumo ou agua? ").strip().lower()
#
# if categoria == "sumo":
#     print("Sumos disponíveis:", ", ".join(sumos))
#     escolha2 = input("Qual sumo? ").strip().lower()
#     if escolha2 in sumos:
#         print(f"🥤 Aqui está o teu sumo de {escolha2}!")
#     else:
#         print(f"❌ Não temos sumo de {escolha2}.")
# else:
#     if categoria == "agua":
#         print("Águas disponíveis:", ", ".join(aguas))
#         escolha2 = input("Qual água? ").strip().lower()
#         if escolha2 in aguas:
#             print(f"💧 Aqui está a tua água {escolha2}!")
#         else:
#             print(f"❌ Não temos água {escolha2}.")
#     else:
#         print("Só temos sumos e águas.")


# ============================================================
# EXTRA 2 — Verificador de ingredientes de receita
# ============================================================
# Tens uma lista de ingredientes no frigorífico.
# O utilizador pede um ingrediente.
# O programa diz se tens ou não tens em casa.
# Se não tiveres, sugere um substituto fixo.
#
# ingredientes = ["ovos", "leite", "farinha", "manteiga", "sal"]
# substitutos (pré-definidos, sem dicionário):
#   manteiga → "margarina"
#   leite    → "leite de aveia"
#   ovos     → "linhaça com água"
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Frigorífico ===")
# ingredientes = ["ovos", "leite", "farinha", "manteiga", "sal"]
# print("No frigorífico:", ", ".join(ingredientes))
#
# pedido = input("Precisas de que ingrediente? ").strip().lower()
#
# if pedido in ingredientes:
#     print(f"✅ Tens {pedido} em casa!")
# else:
#     print(f"❌ Não tens {pedido}.")
#     if pedido == "manteiga":
#         print("💡 Substituto: margarina")
#     else:
#         if pedido == "leite":
#             print("💡 Substituto: leite de aveia")
#         else:
#             if pedido == "ovos":
#                 print("💡 Substituto: linhaça com água")
#             else:
#                 print("Sem substituto sugerido.")


# ============================================================
# EXTRA 3 — Quiz de capitais com lista de respostas válidas
# ============================================================
# Algumas cidades têm nomes alternativos aceites.
# Usa uma lista de respostas válidas para cada pergunta.
# O operador "in" verifica se a resposta do utilizador
# está dentro das respostas aceites.
#
# Exemplo:
#   validas_1 = ["lisboa", "lx", "lisbon"]
#   if resposta in validas_1: → aceita qualquer das 3 formas
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Quiz de Capitais ===")
# pontos = 0
#
# # Pergunta 1
# print("Qual é a capital de Portugal?")
# r1 = input("Resposta: ").strip().lower()
# validas_1 = ["lisboa", "lisbon", "lx"]
# if r1 in validas_1:
#     print("✅ Certo!")
#     pontos += 1
# else:
#     print("❌ Errado. É Lisboa.")
#
# # Pergunta 2
# print("\nQual é a capital de Espanha?")
# r2 = input("Resposta: ").strip().lower()
# validas_2 = ["madrid", "madrid espanha"]
# if r2 in validas_2:
#     print("✅ Certo!")
#     pontos += 1
# else:
#     print("❌ Errado. É Madrid.")
#
# print(f"\nPontuação: {pontos} / 2")
