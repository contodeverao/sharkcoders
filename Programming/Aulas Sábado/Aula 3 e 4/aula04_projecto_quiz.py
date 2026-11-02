# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 04 — PROJECTO: Mini-Quiz de 5 Perguntas
# ============================================================
# Conceitos: tudo das aulas 01 a 04
#   print(), input(), f-strings, if/elif/else, .lower(), .strip()
#   variável acumuladora (pontuacao += 1)
# ============================================================


# ------------------------------------------------------------
# SOBRE ESTE PROJECTO
# ------------------------------------------------------------
# O Mini-Quiz é o primeiro programa completo do curso.
# Usa tudo o que aprendeste nas aulas 01 a 04:
#   • print() e formatação (Aula 01)
#   • input(), f-strings, .strip()/.lower() (Aula 02)
#   • if/elif/else para verificar respostas (Aula 03)
#   • Vários elif para feedback final personalizado (Aula 03)
#
# PADRÃO de cada pergunta (repete-se 5 vezes):
#   1. Mostrar a pergunta com print()
#   2. Receber a resposta com input() + .strip()/.lower()
#   3. Verificar com if/else
#   4. Dar feedback imediato
#   5. Se correcto → pontuacao += 1
# ------------------------------------------------------------


# ── BOAS-VINDAS ───────────────────────────────────────────────

print("\n" + "=" * 50)
print("         BEM-VINDO AO MINI-QUIZ!")
print("         SharkCoders — Python 1º Ano")
print("=" * 50)

nome_jogador = input("\nComo te chamas? ")
print(f"\nOlá, {nome_jogador}! Vamos começar.")
print("5 perguntas — 1 ponto por resposta certa.")
print("-" * 50)

pontuacao = 0   # variável acumuladora — começa em 0


# ── PERGUNTA 1 ───────────────────────────────────────────────

print("\nPERGUNTA 1 de 5")
print("Em que ano foi criado o Python?")
r1 = input("A tua resposta: ").strip()

if r1 == "1991":
    print("✅ CERTO! O Python foi criado em 1991 por Guido van Rossum.")
    pontuacao += 1
else:
    print("❌ Errado. A resposta certa era: 1991")


# ── PERGUNTA 2 ───────────────────────────────────────────────

print("\nPERGUNTA 2 de 5")
print("Qual é o resultado de 2 ** 10 em Python?")
r2 = input("A tua resposta: ").strip()

if r2 == "1024":
    print("✅ CERTO! 2 elevado a 10 = 1024.")
    pontuacao += 1
else:
    print("❌ Errado. A resposta certa era: 1024")
    print("   Dica: 2**10 = 2×2×2×2×2×2×2×2×2×2 = 1024")


# ── PERGUNTA 3 ───────────────────────────────────────────────

print("\nPERGUNTA 3 de 5")
print("Qual função usamos para mostrar texto no ecrã?")
r3 = input("A tua resposta: ").strip().lower()

if r3 == "print" or r3 == "print()":
    print("✅ CERTO! A função print() mostra texto no ecrã.")
    pontuacao += 1
else:
    print("❌ Errado. A resposta certa era: print()")


# ── PERGUNTA 4 ───────────────────────────────────────────────

print("\nPERGUNTA 4 de 5")
print("Qual é o tipo (type) de:  \"SharkCoders\"")
print("  a) int    b) float    c) str    d) bool")
r4 = input("A tua resposta (a/b/c/d): ").strip().lower()

if r4 == "c" or r4 == "str":
    print("✅ CERTO! \"SharkCoders\" é uma string (str).")
    pontuacao += 1
else:
    print("❌ Errado. A resposta certa era: c) str")


# ── PERGUNTA 5 ───────────────────────────────────────────────

print("\nPERGUNTA 5 de 5")
print("Qual palavra usamos em Python para dizer 'SENÃO SE'?")
r5 = input("A tua resposta: ").strip().lower()

if r5 == "elif":
    print("✅ CERTO! 'elif' significa 'else if' — senão se.")
    pontuacao += 1
else:
    print("❌ Errado. A resposta certa era: elif")


# ── RESULTADO FINAL ──────────────────────────────────────────

percentagem = pontuacao * 20   # cada pergunta vale 20%

print("\n" + "=" * 50)
print(f"     RESULTADO FINAL — {nome_jogador.upper()}")
print("=" * 50)
print(f"\n  Pontuação:    {pontuacao} / 5")
print(f"  Percentagem:  {percentagem}%")

if pontuacao == 5:
    print("\n  🏆 PERFEITO! És um craque do Python!")
elif pontuacao >= 4:
    print("\n  🌟 EXCELENTE! Quase perfeito!")
elif pontuacao >= 3:
    print("\n  👍 BOM! Mais de metade certa!")
elif pontuacao >= 2:
    print("\n  📚 Continua a estudar — consegues melhorar!")
else:
    print("\n  💪 Não desistas! Revê as aulas e tenta de novo.")

print("\n" + "=" * 50)
print(f"  Obrigado por jogares, {nome_jogador}!")
print("=" * 50)


# ============================================================
# EXTRA 1 — Respostas múltiplas válidas
# ============================================================
# Algumas perguntas aceitam mais do que uma resposta certa.
# Usa "or" para aceitar variações da mesma resposta.
#
# Exemplo: "print" e "print()" devem ser ambas aceites.
# Adapta TODAS as 5 perguntas do quiz para aceitar variações.
#
# Pergunta 1: "1991" (só uma forma possível)
# Pergunta 2: "1024" (só uma forma possível)
# Pergunta 3: "print" or "print()" ← já está feito!
# Pergunta 4: "c" or "str" ← já está feito!
# Pergunta 5: "elif" or "else if" or "senão se"
#
# Dica: experimenta errar de propósito e verifica se a tua
# versão aceita todas as formas correctas.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# (copia o quiz completo e adiciona as variações com "or")


# ============================================================
# EXTRA 2 — Dificuldade à escolha
# ============================================================
# Antes de começar o quiz, pergunta ao jogador o nível
# de dificuldade: fácil, médio ou difícil.
#
# Fácil:  mostrar uma dica antes de cada pergunta
# Médio:  sem dicas (o quiz normal)
# Difícil: sem dicas + mostrar "Errado" mas NÃO a resposta certa
#
# Usa if/elif/else para controlar o comportamento
# de cada pergunta conforme o nível escolhido.
#
# Exemplo de dica para a pergunta 1:
#   "Dica: foi criado no mesmo ano em que a internet começou
#    a ser usada pelo público geral."
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# nivel = input("Nível (facil/medio/dificil): ").strip().lower()
#
# # Pergunta 1
# if nivel == "facil":
#     print("💡 Dica: foi nos anos 90, logo no início da década.")
# print("Em que ano foi criado o Python?")
# r1 = input("Resposta: ").strip()
# if r1 == "1991":
#     print("✅ CERTO!")
#     pontuacao += 1
# else:
#     if nivel == "dificil":
#         print("❌ Errado.")
#     else:
#         print("❌ Errado. A resposta certa era: 1991")


# ============================================================
# EXTRA 3 — O TEU PRÓPRIO QUIZ
# ============================================================
# Cria a tua versão do quiz sobre um tema que gostes!
# Usa APENAS o que aprendeste nas aulas 01 a 04.
#
# Requisitos:
#   ✅ 5 perguntas sobre o teu tema favorito
#   ✅ Pelo menos 1 pergunta com escolha múltipla (a/b/c/d)
#   ✅ Pelo menos 1 pergunta com resposta numérica
#   ✅ .lower() e .strip() em todas as respostas de texto
#   ✅ "or" para aceitar variações de resposta
#   ✅ Feedback personalizado no fim com 5 níveis (if/elif/else)
#   ✅ Pontuação em fracção E em percentagem
#
# Ideias de temas:
#   🎮 Videojogos    🎵 Música    ⚽ Futebol
#   🎬 Filmes        🐍 Python    🌍 Geografia
# ============================================================

# ESCREVE O TEU QUIZ AQUI:
# print("\n=== O MEU QUIZ SOBRE [TEMA] ===")
# nome2 = input("Nome do jogador: ")
# pontuacao2 = 0
#
# # Pergunta 1
# print("\nPERGUNTA 1 de 5")
# print("...")
# r1 = input("Resposta: ").strip().lower()
# if r1 == "..." or r1 == "...":
#     print("✅ CERTO!")
#     pontuacao2 += 1
# else:
#     print("❌ Errado. A resposta certa era: ...")
#
# # [repetir para perguntas 2 a 5]
#
# # Resultado final
# print(f"\nPontuação: {pontuacao2} / 5")
# print(f"Percentagem: {pontuacao2 * 20}%")
# if pontuacao2 == 5:
#     print("🏆 PERFEITO!")
# elif pontuacao2 >= 4:
#     print("🌟 EXCELENTE!")
# elif pontuacao2 >= 3:
#     print("👍 BOM!")
# elif pontuacao2 >= 2:
#     print("📚 Continua a estudar!")
# else:
#     print("💪 Não desistas!")
