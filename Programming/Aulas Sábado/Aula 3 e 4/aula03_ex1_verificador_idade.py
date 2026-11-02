# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 03 — Exercício 1: Verificador de Idade
# ============================================================
# Conceitos: if / else, operadores de comparação >= !=
# ============================================================


# ------------------------------------------------------------
# CONCEITO — if / else
# ------------------------------------------------------------
# O if verifica uma condição e executa código SE for True.
# O else executa código SE a condição for False.
#
# Operadores de comparação (devolvem True ou False):
#   ==   igual a          10 == 10 → True
#   !=   diferente de     10 != 5  → True
#   >    maior que        10 > 5   → True
#   <    menor que        5  < 10  → True
#   >=   maior ou igual   10 >= 10 → True
#   <=   menor ou igual   5  <= 10 → True
#
# ATENÇÃO:  =  é para guardar valores  (idade = 18)
#           == é para comparar         (idade == 18)
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────
# Pede a idade ao utilizador.
# SE tiver 18 ou mais → mostrar que é maior de idade
# SENÃO → mostrar quantos anos faltam

print("=== Verificador de Idade ===")

idade = int(input("Qual é a tua idade? "))

if idade >= 18:
    print("✅ És maior de idade.")
    print("Podes conduzir, votar e ver filmes para adultos!")
else:
    print("❌ Ainda és menor de idade.")
    anos_faltam = 18 - idade
    print(f"Faltam {anos_faltam} anos para seres maior de idade.")

print("\nPrograma terminado.")   # esta linha corre SEMPRE


# ============================================================
# EXTRA 1 — Adicionar verificação para idades inválidas
# ============================================================
# Modifica o programa para verificar se a idade é válida.
# Uma idade válida é entre 0 e 120 anos.
# Se a idade for inválida, mostrar uma mensagem de erro
# e NÃO continuar para a verificação de maior/menor.
#
# Dica: usa um if separado NO INÍCIO só para validar.
#       Se for inválida, mostra o erro e termina esse bloco.
#       Se for válida, usa o if/else normal a seguir.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Com validação ===")
# idade2 = int(input("Idade (versão com validação): "))
#
# if idade2 < 0 or idade2 > 120:
#     print("Idade inválida! Tem de ser entre 0 e 120.")
# else:
#     if idade2 >= 18:
#         print("Maior de idade.")
#     else:
#         print(f"Menor de idade. Faltam {18 - idade2} anos.")


# ============================================================
# EXTRA 2 — Maior, menor ou igual a 18
# ============================================================
# Alarga o programa com mais um caso:
#   • Exactamente 18 anos  → "Acabaste de ser maior de idade!"
#   • Mais de 18 anos      → "Já és maior de idade há X anos."
#   • Menos de 18 anos     → "Faltam X anos."
#
# Dica: usa if/else aninhados (if dentro de if).
#       Primeiro verifica se é >= 18.
#       Dentro desse bloco, verifica se é == 18 ou > 18.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Exactamente 18? ===")
# idade3 = int(input("Idade: "))
#
# if idade3 >= 18:
#     if idade3 == 18:
#         print("🎉 Acabaste de ser maior de idade!")
#     else:
#         print(f"Já és maior de idade há {idade3 - 18} anos.")
# else:
#     print(f"Faltam {18 - idade3} anos para seres maior de idade.")


# ============================================================
# EXTRA 3 — Maior de idade em diferentes países
# ============================================================
# A maioridade varia por país:
#   • Portugal, Brasil:  18 anos
#   • Japão:             20 anos  (desde 2022 mudou para 18)
#   • EUA:               21 anos (para álcool)
#   • Coreia do Sul:     19 anos
#
# Pede a idade e o país.
# Mostra se a pessoa é maior de idade NESSE país.
# Usa apenas if/else — um para cada país.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Maioridade por país ===")
# idade4 = int(input("Idade: "))
# pais   = input("País (portugal/japao/eua/coreia): ").strip().lower()
#
# if pais == "portugal":
#     if idade4 >= 18:
#         print("✅ Maior de idade em Portugal.")
#     else:
#         print(f"❌ Menor de idade. Faltam {18 - idade4} anos.")
# else:
#     if pais == "japao":
#         limite = 18
#     else:
#         if pais == "eua":
#             limite = 21
#         else:
#             limite = 19   # coreia do sul
#     if idade4 >= limite:
#         print(f"✅ Maior de idade em {pais} (limite: {limite} anos).")
#     else:
#         print(f"❌ Faltam {limite - idade4} anos.")
