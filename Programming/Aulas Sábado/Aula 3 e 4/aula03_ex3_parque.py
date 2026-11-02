# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 03 — Exercício 3: Parque de Diversões
# ============================================================
# Conceitos: and, or, not, .lower(), .strip()
# ============================================================


# ------------------------------------------------------------
# CONCEITO — and / or / not
# ------------------------------------------------------------
# Combinam várias condições numa só:
#
#   and → E    — ambas têm de ser True
#               altura>=140 and tem_bilhete=="sim"
#               → só entra se tiver altura E bilhete
#
#   or  → OU   — basta uma ser True
#               nota<0 or nota>20
#               → inválida se menor que 0 OU maior que 20
#
#   not → NÃO  — inverte o resultado
#               not e_chovendo
#               → True se NÃO estiver a chover
#
# .lower()  → converte texto para minúsculas
#             "Sim" / "SIM" / "sim" → todos ficam "sim"
# .strip()  → remove espaços antes e depois do texto
#             "  sim  " → "sim"
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────
# Para entrar no parque de diversões precisas de:
#   • Ter pelo menos 140 cm de altura
#   • Ter bilhete
# Mostra a mensagem correcta para cada combinação.

print("=== Parque de Diversões ===")

altura_cm   = int(input("Qual é a tua altura em cm? "))
tem_bilhete = input("Tens bilhete? (sim/nao) ").strip().lower()

if altura_cm >= 140 and tem_bilhete == "sim":
    print("🎢 Bem-vindo! Podes entrar e andar em todas as atracções!")
elif altura_cm < 140 and tem_bilhete == "sim":
    print("⚠️  Tens bilhete mas és baixo demais para algumas atracções.")
    print("   Podes entrar mas só nas atracções para crianças.")
elif altura_cm >= 140 and tem_bilhete == "nao":
    print("🎫 Tens altura suficiente mas precisas de comprar bilhete.")
    print("   A bilheteira fica à entrada.")
else:
    print("❌ Não podes entrar: precisas de bilhete E de ter 140+ cm.")


# ============================================================
# EXTRA 1 — Adicionar verificação de acompanhante
# ============================================================
# Adiciona uma terceira condição:
#   • Se tiver menos de 12 anos → precisa de acompanhante adulto
#
# Pede também a idade. Se a pessoa tiver menos de 12 anos
# e não tiver acompanhante, não pode entrar mesmo com bilhete.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Com acompanhante ===")
# altura2      = int(input("Altura (cm): "))
# idade2       = int(input("Idade: "))
# bilhete2     = input("Tens bilhete? (sim/nao) ").strip().lower()
# acompanhante = input("Tens acompanhante adulto? (sim/nao) ").strip().lower()
#
# if bilhete2 != "sim":
#     print("Precisas de bilhete para entrar.")
# elif altura2 < 140:
#     print("Não tens altura suficiente (mínimo 140cm).")
# elif idade2 < 12 and acompanhante != "sim":
#     print("Tens menos de 12 anos — precisas de acompanhante.")
# else:
#     print("Bem-vindo ao parque!")


# ============================================================
# EXTRA 2 — Tabela de preços por altura e idade
# ============================================================
# O parque tem preços diferentes:
#   • Menos de 100cm:   GRÁTIS
#   • 100 a 139cm:      8€  (atracções infantis)
#   • 140cm ou mais
#       < 65 anos:      15€ (acesso total)
#       >= 65 anos:     10€ (desconto sénior)
#
# Pede a altura e a idade e mostra o preço correcto.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Tabela de preços ===")
# altura3 = int(input("Altura (cm): "))
# idade3  = int(input("Idade: "))
#
# if altura3 < 100:
#     print("Entrada GRÁTIS!")
# elif altura3 < 140:
#     print("Bilhete: 8€ (zona infantil)")
# elif idade3 >= 65:
#     print("Bilhete: 10€ (desconto sénior)")
# else:
#     print("Bilhete: 15€ (acesso total)")


# ============================================================
# EXTRA 3 — Verificador de acesso a atracção específica
# ============================================================
# A montanha-russa "Shark Coaster" tem regras especiais:
#   • Altura mínima: 150cm
#   • Idade mínima: 12 anos
#   • Problemas de saúde (cardíacos, grávidas): NÃO podem entrar
#   • Precisa de bilhete geral
#
# Cria o verificador completo para esta atracção.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 3: Shark Coaster ===")
# altura4      = int(input("Altura (cm): "))
# idade4       = int(input("Idade: "))
# bilhete4     = input("Tens bilhete? (sim/nao) ").strip().lower()
# saude_ok     = input("Sem problemas de saúde? (sim/nao) ").strip().lower()
#
# if bilhete4 != "sim":
#     print("Precisas de bilhete geral.")
# elif altura4 < 150:
#     print(f"Altura mínima: 150cm. Faltam {150 - altura4}cm.")
# elif idade4 < 12:
#     print(f"Idade mínima: 12 anos. Faltam {12 - idade4} anos.")
# elif saude_ok != "sim":
#     print("Por razões de segurança não podes entrar nesta atracção.")
# else:
#     print("✅ Podes entrar no Shark Coaster! Boa sorte! 🦈")
