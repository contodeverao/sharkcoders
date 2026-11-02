10# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 03 — Exercício 2: Classificação de Notas
# ============================================================
# Conceitos: if / elif / else, múltiplas condições, or
# ============================================================


# ------------------------------------------------------------
# CONCEITO — elif (senão se)
# ------------------------------------------------------------
# Quando temos mais de 2 situações, usamos elif.
# O Python verifica as condições PELA ORDEM em que estão
# e PARA quando encontra a primeira que é True.
#
# Por isso: as condições mais restritas têm de vir PRIMEIRO!
#   ❌ ERRADO:  elif nota >= 10: ... elif nota >= 18: ...
#       (nota 19 entra no >= 10 e nunca chega ao >= 18!)
#   ✅ CERTO:   elif nota >= 18: ... elif nota >= 10: ...
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────
# Pede uma nota de 0 a 20 e classifica:
#   Inválida:       nota fora de [0, 20]
#   Muito Bom:      >= 18
#   Bom:            >= 14
#   Suficiente:     >= 10
#   Insuficiente:   < 10

print("=== Classificação de Notas (0-20) ===")

nota = int(input("Qual foi a tua nota? "))

if nota < 0 or nota > 20:
    print("❌ Nota inválida! Tem de ser entre 0 e 20.")
elif nota >= 18:
    print("🏆 Muito Bom! Excelente resultado!")
elif nota >= 14:
    print("👍 Bom! Continua assim!")
elif nota >= 10:
    print("✅ Suficiente. Passaste, mas podes melhorar.")
else:
    print("❌ Insuficiente. Não passaste desta vez.")


# ============================================================
# EXTRA 1 — Adicionar a nota mínima de aprovação exacta
# ============================================================
# Adiciona um elif específico para nota == 10 que mostre:
# "Passou com a nota mínima! Atenção ao próximo teste."
#
# Dica: tem de aparecer ANTES do elif nota >= 10
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Com nota mínima ===")
# nota2 = int(input("Nota: "))
#
# if nota2 < 0 or nota2 > 20:
#     print("Inválida.")
# elif nota2 >= 18:
#     print("Muito Bom!")
# elif nota2 >= 14:
#     print("Bom!")
# elif nota2 == 10:
#     print("Passou com a nota mínima! Atenção ao próximo teste.")
# elif nota2 >= 10:
#     print("Suficiente.")
# else:
#     print("Insuficiente.")


# ============================================================
# EXTRA 2 — Mostrar o que falta para a próxima classificação
# ============================================================
# No fim do programa, mostra também o que falta para
# a próxima classificação. Exemplo:
#   nota = 12 → "Faltam 2 pontos para Bom (14)"
#   nota = 16 → "Faltam 2 pontos para Muito Bom (18)"
#   nota = 19 → "Já tens Muito Bom — continua!"
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Quanto falta? ===")
# nota3 = int(input("Nota: "))
#
# if nota3 < 0 or nota3 > 20:
#     print("Inválida.")
# elif nota3 >= 18:
#     print("Muito Bom! Já estás no topo!")
# elif nota3 >= 14:
#     print("Bom!")
#     print(f"Faltam {18 - nota3} pontos para Muito Bom.")
# elif nota3 >= 10:
#     print("Suficiente.")
#     print(f"Faltam {14 - nota3} pontos para Bom.")
# else:
#     print("Insuficiente.")
#     print(f"Faltam {10 - nota3} pontos para Suficiente.")


# ============================================================
# EXTRA 3 — Boletim completo com 3 disciplinas
# ============================================================
# Pede a nota de 3 disciplinas (ex: Português, Matemática, inglês).
# Para cada uma, mostra a classificação.
# No final, calcula a média e classifica também a média.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Boletim ===")
# nota_port = int(input("Nota de Português (0-20): "))
# nota_mat  = int(input("Nota de Matemática (0-20): "))
# nota_ing  = int(input("Nota de Inglês (0-20): "))
#
# media = (nota_port + nota_mat + nota_ing) / 3
# print(f"\nMédia: {media:.1f}")
#
# if media >= 18:
#     print("Classificação geral: Muito Bom!")
# elif media >= 14:
#     print("Classificação geral: Bom!")
# elif media >= 10:
#     print("Classificação geral: Suficiente.")
# else:
#     print("Classificação geral: Insuficiente.")
