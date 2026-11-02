# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 04 — Exercício 3: Operador Ternário
# ============================================================
# Conceitos: operador ternário, % (resto), abs()
# ============================================================


# ------------------------------------------------------------
# CONCEITO — Operador Ternário
# ------------------------------------------------------------
# O ternário permite escrever um if/else simples numa linha.
# Útil quando apenas queremos atribuir um de dois valores.
#
# FORMA LONGA (3 linhas):
#   if condição:
#       resultado = "valor A"
#   else:
#       resultado = "valor B"
#
# FORMA CURTA — ternário (1 linha):
#   resultado = "valor A" if condição else "valor B"
#
# Lê-se: "resultado é 'valor A' SE condição, SENÃO 'valor B'"
#
# QUANDO USAR:
#   ✅ Condição simples, só dois resultados possíveis
#   ❌ Condição complexa ou mais de dois resultados
#      (nesse caso usar if/elif/else normal — mais legível)
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────

print("=== Operador Ternário ===")
numero = int(input("Escreve um número: "))

# Par ou ímpar — o % dá o resto da divisão
# Se o resto de dividir por 2 for 0 → é par
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"{numero} é {resultado}")

# Positivo, negativo ou zero — ternário encadeado
sinal = "positivo" if numero > 0 else ("zero" if numero == 0 else "negativo")
print(f"{numero} é {sinal}")

# Temperatura com ternário
print()
temperatura = int(input("Temperatura hoje (°C): "))
clima = "quente" if temperatura >= 25 else ("ameno" if temperatura >= 15 else "frio")
print(f"Hoje está {clima} ({temperatura}°C)")

# TAREFA: reescreve a linha do clima como um if/elif/else normal
# e vê qual a diferença de legibilidade:
# if temperatura >= 25:
#     clima2 = "quente"
# elif temperatura >= 15:
#     clima2 = "ameno"
# else:
#     clima2 = "frio"


# ============================================================
# EXTRA 1 — Conversor de letras com ternário
# ============================================================
# Pede uma letra ao utilizador.
# Com ternário, verifica se é maiúscula ou minúscula.
# Mostra a versão oposta.
#
# Dica: .isupper() → True se for maiúscula
#       .upper()   → converte para maiúscula
#       .lower()   → converte para minúscula
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Conversor de letras ===")
# letra = input("Escreve uma letra: ")[0]   # [0] pega só o 1º caracter
#
# tipo = "maiúscula" if letra.isupper() else "minúscula"
# oposta = letra.lower() if letra.isupper() else letra.upper()
# print(f"'{letra}' é {tipo}. Versão oposta: '{oposta}'")


# ============================================================
# EXTRA 2 — Verificador de ano bissexto com ternário
# ============================================================
# Um ano é bissexto se:
#   • É divisível por 4 E
#   • NÃO é divisível por 100, OU é divisível por 400
#
# Fórmula: (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
#
# Usa o ternário para mostrar "bissexto" ou "não bissexto".
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Ano bissexto ===")
# ano = int(input("Ano: "))
# bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
# resultado_biss = "bissexto" if bissexto else "não bissexto"
# print(f"{ano} é {resultado_biss}.")


# ============================================================
# EXTRA 3 — Calculadora de desconto com ternário
# ============================================================
# Uma loja dá desconto baseado no valor total da compra:
#   >= 100€ → 15% de desconto
#   >= 50€  → 10% de desconto
#   < 50€   → sem desconto
#
# Usa ternário encadeado para calcular a percentagem de desconto.
# Mostra o preço original, o desconto e o preço final.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Desconto de loja ===")
# total = float(input("Total da compra (€): "))
#
# desconto = 0.15 if total >= 100 else (0.10 if total >= 50 else 0.0)
# valor_desconto = total * desconto
# preco_final    = total - valor_desconto
#
# print(f"Preço original:  {total:.2f}€")
# print(f"Desconto ({int(desconto*100)}%): -{valor_desconto:.2f}€")
# print(f"Preço final:     {preco_final:.2f}€")
