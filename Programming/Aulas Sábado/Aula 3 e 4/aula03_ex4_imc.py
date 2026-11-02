# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 03 — Exercício 4: Calculadora de IMC
# ============================================================
# Conceitos: if/elif/else, float(), f-strings com :.2f
# Ligação: retoma o desafio extra da Aula 02!
# ============================================================


# ------------------------------------------------------------
# CONCEITO — Retomar o desafio da Aula 02
# ------------------------------------------------------------
# Na Aula 02, o desafio extra pedia para calcular o IMC.
# Ficou a faltar a parte das condições — agora completamos!
#
# IMC = peso (kg) / altura² (m)
#
# Classificação OMS:
#   IMC < 18.5         → Baixo Peso
#   18.5 <= IMC < 25   → Peso Normal
#   25   <= IMC < 30   → Excesso de Peso
#   IMC >= 30          → Obesidade
#
# Padrão eficiente: guardar o resultado numa variável
# e usar um único print no fim — evita repetir código.
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────

print("=== Calculadora de IMC ===\n")

nome   = input("Nome: ")
peso   = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Calcular o IMC
imc = peso / (altura ** 2)

print(f"\nOlá, {nome}!")
print(f"IMC = {imc:.2f}")       # :.2f → 2 casas decimais

# Classificar — padrão eficiente com variável categoria
if imc < 18.5:
    categoria = "Baixo Peso"
elif imc < 25:
    categoria = "Peso Normal"
elif imc < 30:
    categoria = "Excesso de Peso"
else:
    categoria = "Obesidade"

print(f"Categoria: {categoria}")


# ============================================================
# EXTRA 1 — Mensagem personalizada por categoria
# ============================================================
# Adiciona uma mensagem de conselho para cada categoria:
#   Baixo Peso:      "Consulta um médico e aumenta a ingestão calórica."
#   Peso Normal:     "Excelente! Mantém os hábitos saudáveis."
#   Excesso de Peso: "Considera aumentar a actividade física."
#   Obesidade:       "Consulta um médico para um plano personalizado."
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# if categoria == "Baixo Peso":
#     print("💡 Consulta um médico e aumenta a ingestão calórica.")
# elif categoria == "Peso Normal":
#     print("✅ Excelente! Mantém os hábitos saudáveis.")
# elif categoria == "Excesso de Peso":
#     print("⚠️  Considera aumentar a actividade física.")
# else:
#     print("❗ Consulta um médico para um plano personalizado.")


# ============================================================
# EXTRA 2 — IMC ideal e diferença
# ============================================================
# O IMC ideal é 22.0 (centro do intervalo Peso Normal).
# Calcula e mostra quanto peso o utilizador precisaria de
# perder ou ganhar para atingir o IMC ideal de 22.0.
#
# Fórmula: peso_ideal = 22.0 * (altura ** 2)
#          diferenca  = peso - peso_ideal
#
# Se diferença > 0 → mostrar quantos kg a perder
# Se diferença < 0 → mostrar quantos kg a ganhar
# Se diferença == 0 → peso perfeito!
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# peso_ideal = 22.0 * (altura ** 2)
# diferenca  = peso - peso_ideal
#
# print(f"\nPeso ideal para a tua altura: {peso_ideal:.1f} kg")
#
# if diferenca > 1:
#     print(f"Para atingir o IMC ideal, precisas de perder {diferenca:.1f} kg.")
# elif diferenca < -1:
#     print(f"Para atingir o IMC ideal, precisas de ganhar {abs(diferenca):.1f} kg.")
# else:
#     print("Estás praticamente no peso ideal!")


# ============================================================
# EXTRA 3 — IMC para crianças (percentil por idade)
# ============================================================
# O IMC para crianças é interpretado de forma diferente.
# Para simplificar, usa estas regras para 10-17 anos:
#
#   IMC < 16:   Baixo Peso
#   16-21:      Peso Normal
#   21-25:      Excesso de Peso
#   >= 25:      Obesidade
#
# Pede a idade. Se tiver menos de 18, usa as regras de criança.
# Se tiver 18 ou mais, usa as regras da OMS (versão base).
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: IMC por faixa etária ===")
# nome3   = input("Nome: ")
# peso3   = float(input("Peso (kg): "))
# altura3 = float(input("Altura (m): "))
# idade3  = int(input("Idade: "))
#
# imc3 = peso3 / (altura3 ** 2)
# print(f"\nIMC de {nome3}: {imc3:.2f}")
#
# if idade3 < 18:
#     print("(Tabela pediátrica simplificada)")
#     if imc3 < 16:
#         print("Baixo Peso")
#     elif imc3 < 21:
#         print("Peso Normal")
#     elif imc3 < 25:
#         print("Excesso de Peso")
#     else:
#         print("Obesidade")
# else:
#     print("(Tabela OMS adultos)")
#     if imc3 < 18.5:
#         print("Baixo Peso")
#     elif imc3 < 25:
#         print("Peso Normal")
#     elif imc3 < 30:
#         print("Excesso de Peso")
#     else:
#         print("Obesidade")
