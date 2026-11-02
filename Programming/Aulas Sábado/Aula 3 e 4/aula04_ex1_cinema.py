# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 04 — Exercício 1: Sistema de Acesso ao Cinema
# ============================================================
# Conceitos: condições aninhadas (if dentro de if)
# ============================================================


# ------------------------------------------------------------
# CONCEITO — Condições aninhadas (nesting)
# ------------------------------------------------------------
# Por vezes a segunda decisão só faz sentido depois da primeira.
# Podemos colocar um if DENTRO de outro if.
#
# Cada nível de aninhamento tem MAIS 4 espaços de indentação:
#   if (nível 1):          → 0 espaços
#       if (nível 2):      → 4 espaços
#           código         → 8 espaços
#       else:              → 4 espaços
#           código         → 8 espaços
#
# Pensa como uma árvore de decisão:
#   Primeiro: maior ou menor de 18?
#   Depois: tem bilhete ou não?
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────
# Sistema de acesso ao cinema com 3 faixas etárias.
# Cada faixa tem depois a questão do bilhete.

print("=== Sistema de Acesso ao Cinema ===")

idade       = int(input("Idade: "))
tem_bilhete = input("Tens bilhete? (sim/nao) ").strip().lower()

if idade >= 18:
    # ── Maiores de idade ──────────────────────────────────
    if tem_bilhete == "sim":
        print("🎬 Bem-vindo! Podes entrar em qualquer sala.")
    else:
        print("🎫 Podes ver qualquer filme, mas precisas de bilhete.")

elif idade >= 12:
    # ── Jovens (12-17 anos) ───────────────────────────────
    if tem_bilhete == "sim":
        print("🎬 Podes entrar, mas apenas em filmes M/12 ou menos.")
    else:
        print("🎫 Precisas de bilhete. Só podes ver filmes M/12.")

else:
    # ── Crianças (menos de 12 anos) ──────────────────────
    print("👨‍👩‍👦 Tens menos de 12 anos.")
    print("   Precisas de um adulto responsável para entrar.")


# ============================================================
# EXTRA 1 — Adicionar verificação do tipo de filme
# ============================================================
# Além da idade e do bilhete, adicionar a classificação do filme:
#   M/4, M/6, M/12, M/16, M/18
#
# Verifica se o utilizador pode ver o filme escolhido.
# Exemplo: pessoa com 15 anos pode ver M/12 mas não M/16.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Com classificação do filme ===")
# idade2   = int(input("Idade: "))
# bilhete2 = input("Tens bilhete? (sim/nao) ").strip().lower()
# filme2   = input("Classificação do filme (4/6/12/16/18): ")
# idade_min = int(filme2)
#
# if bilhete2 != "sim":
#     print("Precisas de bilhete.")
# elif idade2 < idade_min:
#     print(f"Não podes ver este filme — classificação M/{filme2}.")
#     print(f"Faltam {idade_min - idade2} anos.")
# else:
#     print(f"✅ Podes entrar! Boa sessão!")


# ============================================================
# EXTRA 2 — Desconto de grupo
# ============================================================
# O cinema tem desconto de grupo para 4 ou mais pessoas.
# Se o grupo tiver 4+ pessoas E todos tiverem bilhete → 20% desconto.
# O preço base do bilhete é 9€.
#
# Pede o número de pessoas e se todos têm bilhete.
# Mostra o preço total com ou sem desconto.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Desconto de grupo ===")
# num_pessoas = int(input("Quantas pessoas no grupo? "))
# todos_bilhete = input("Todos têm bilhete? (sim/nao) ").strip().lower()
#
# preco_base = 9.0
# if num_pessoas >= 4 and todos_bilhete == "sim":
#     desconto   = 0.20
#     preco_final = preco_base * (1 - desconto) * num_pessoas
#     print(f"🎉 Desconto de grupo de 20%!")
#     print(f"Total: {preco_final:.2f}€ ({num_pessoas} × {preco_base * 0.8:.2f}€)")
# else:
#     preco_final = preco_base * num_pessoas
#     print(f"Total: {preco_final:.2f}€ ({num_pessoas} × {preco_base:.2f}€)")
#     if num_pessoas < 4:
#         print(f"Dica: com {4 - num_pessoas} pessoas a mais terias 20% desconto!")


# ============================================================
# EXTRA 3 — Sistema completo de cinema
# ============================================================
# Combinar tudo num único sistema:
#   1. Pedir: idade, tem bilhete, classificação do filme, nº pessoas
#   2. Verificar acesso (idade vs classificação)
#   3. Calcular preço (com desconto de grupo se aplicável)
#   4. Mostrar resumo final
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Cinema completo ===")
# ...
