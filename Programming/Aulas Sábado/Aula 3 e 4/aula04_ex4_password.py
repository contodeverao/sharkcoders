# ============================================================
# SHARKCODERS — Python 1º Ano
# AULA 04 — Exercício 4: Verificador de Password
# ============================================================
# Conceitos: any(), isdigit(), isupper(), islower(), len()
# ============================================================


# ------------------------------------------------------------
# CONCEITO — len(), any() e métodos de string
# ------------------------------------------------------------
#
# len() — contar caracteres
#   Já usaste len() na Aula 02 para contar letras de um nome.
#   Aqui usamos para saber o tamanho da password:
#     len("olá")        → 3
#     len("SharkCode")  → 9
#     len("abc123")     → 6
#
# ── Métodos de string — verificar um caracter ─────────────
#   Cada caracter de uma string pode ser verificado com:
#     char.isdigit()  → True se for número   ('3'.isdigit() → True)
#     char.isupper()  → True se for maiúscula ('A'.isupper() → True)
#     char.islower()  → True se for minúscula ('a'.islower() → True)
#     char.isalpha()  → True se for letra     ('a'.isalpha() → True)
#
# ── any() — verificar TODOS os caracteres de uma vez ──────
#   any() percorre cada caracter da string e pergunta:
#   "pelo menos UM satisfaz a condição?"
#   Devolve True se SIM, False se NENHUM.
#
#   A sintaxe  any(c.isdigit() for c in password)  lê-se assim:
#   "para cada caracter c dentro de password,
#    verifica se c é dígito — se pelo menos um for, devolve True"
#
#   O  for c in password  é um for especial — só existe dentro
#   do any(). Não precisas de saber for ainda para o usar aqui.
#   Na Aula 05 vais aprender o for em detalhe!
#
#   Exemplos:
#     any(c.isdigit() for c in "abc3")  → True  (o '3' é dígito)
#     any(c.isdigit() for c in "abcd")  → False (nenhum é dígito)
#     any(c.isupper() for c in "Hello") → True  (o 'H' é maiúscula)
# ------------------------------------------------------------


# ── EXERCÍCIO ────────────────────────────────────────────────

print("=== Verificador de Password ===\n")

password = input("Cria uma password: ")

# Verificar cada critério — cada um é uma variável bool
tem_tamanho   = len(password) >= 8
tem_numero    = any(c.isdigit() for c in password)
tem_maiuscula = any(c.isupper() for c in password)

# Mostrar resultado de cada critério com ✅ ou ❌
print(f"\n{'✅' if tem_tamanho   else '❌'} Pelo menos 8 caracteres ({len(password)} encontrados)")
print(f"{'✅' if tem_numero    else '❌'} Pelo menos 1 número")
print(f"{'✅' if tem_maiuscula  else '❌'} Pelo menos 1 letra maiúscula")

# Avaliação final
if tem_tamanho and tem_numero and tem_maiuscula:
    print("\n🔒 Password FORTE! Boa escolha.")
elif tem_tamanho and (tem_numero or tem_maiuscula):
    print("\n⚠️  Password MÉDIA. Adiciona mais complexidade.")
else:
    print("\n❗ Password FRACA! Torna-a mais segura.")


# ============================================================
# EXTRA 1 — Adicionar critério de caracter especial
# ============================================================
# Uma password ainda mais forte tem pelo menos 1 caracter especial.
# Caracteres especiais: ! @ # $ % ^ & * ( ) _ - + =
#
# Adiciona este critério à verificação e actualiza a avaliação:
#   FORTE:   tamanho + número + maiúscula + especial
#   BOA:     tamanho + número + maiúscula (sem especial)
#   MÉDIA:   tamanho + (número OU maiúscula)
#   FRACA:   tudo o resto
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 1: Com caracter especial ===")
# password2    = input("Password: ")
# especiais    = "!@#$%^&*()-_+=<>?"
#
# t2 = len(password2) >= 8
# n2 = any(c.isdigit() for c in password2)
# m2 = any(c.isupper() for c in password2)
# e2 = any(c in especiais for c in password2)
#
# print(f"{'✅' if t2 else '❌'} 8+ caracteres")
# print(f"{'✅' if n2 else '❌'} 1+ número")
# print(f"{'✅' if m2 else '❌'} 1+ maiúscula")
# print(f"{'✅' if e2 else '❌'} 1+ caracter especial")
#
# if t2 and n2 and m2 and e2:
#     print("🔒 FORTE!")
# elif t2 and n2 and m2:
#     print("👍 BOA!")
# elif t2 and (n2 or m2):
#     print("⚠️  MÉDIA.")
# else:
#     print("❗ FRACA!")


# ============================================================
# EXTRA 2 — Verificador com pontuação
# ============================================================
# Em vez de forte/média/fraca, calcula uma pontuação de 0 a 5:
#   +1 ponto por cada critério satisfeito:
#     • 8+ caracteres
#     • 12+ caracteres (bónus)
#     • 1+ número
#     • 1+ maiúscula
#     • 1+ caracter especial
#
# Mostra a barra de força com os pontos acumulados.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# print("\n=== Extra 2: Pontuação ===")
# pw3      = input("Password: ")
# especiais3 = "!@#$%^&*()-_+="
#
# pontos = 0
# pontos += 1 if len(pw3) >= 8  else 0
# pontos += 1 if len(pw3) >= 12 else 0
# pontos += 1 if any(c.isdigit() for c in pw3) else 0
# pontos += 1 if any(c.isupper() for c in pw3) else 0
# pontos += 1 if any(c in especiais3 for c in pw3) else 0
#
# barra = "█" * pontos + "░" * (5 - pontos)
# print(f"Força: [{barra}] {pontos}/5")
#
# nivel = "Muito Fraca" if pontos<=1 else ("Fraca" if pontos<=2 else
#         ("Média" if pontos==3 else ("Forte" if pontos==4 else "Muito Forte")))
# print(f"Nível: {nivel}")


# ============================================================
# EXTRA 3 — Gerador de password segura
# ============================================================
# Cria um programa que sugere uma password segura aleatória
# com 12 caracteres: letras, números e caracteres especiais.
#
# import random
# import string
#
# letras    = string.ascii_letters    # a-z + A-Z
# numeros   = string.digits           # 0-9
# especiais = "!@#$%^&*"
# todos     = letras + numeros + especiais
#
# Garante pelo menos 1 maiúscula, 1 número e 1 especial.
# ============================================================

# ESCREVE O TEU CÓDIGO AQUI:
# import random
# import string
#
# print("\n=== Extra 3: Gerador de password ===")
# letras    = string.ascii_letters
# numeros   = string.digits
# especiais = "!@#$%^&*"
# todos     = letras + numeros + especiais
#
# # Garantir pelo menos 1 de cada tipo obrigatório
# pw_lista = [
#     random.choice(string.ascii_uppercase),   # 1 maiúscula
#     random.choice(numeros),                   # 1 número
#     random.choice(especiais),                 # 1 especial
#     *[random.choice(todos) for _ in range(9)] # 9 aleatórios
# ]
#
# random.shuffle(pw_lista)             # baralhar a ordem
# password_gerada = "".join(pw_lista)
# print(f"Password sugerida: {password_gerada}")
