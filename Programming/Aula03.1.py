import os
import shutil

print("=== Organizador de Ficheiros ===")

# 1) menu de escolha
print("\nO que pretende organizar")
print("1. Imagens")
print("2. Documentos")
print("3. Planilhas")
print("4. Audio")
print("5. Videos")
print("6. Codigos")
print("7. Tudo")

opcao = input("Escolha uma opcao (1 a 7): ").strip()

# 2) caminho da pasta a organizar
pasta = input("Digite o caminho da pasta que deseja organizar: ").strip()

# 3) categorias com extensoes
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Planilhas": [".xlsx", ".xls", ".csv", ".ods"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Codigos": [".py", ".js", ".ts", ".html", ".css", ".json", ".xml"],
    "Outros": []
}

# 4) filtrar categorias conforme a escolha do menu
mapa_opcoes = {
    "1": ["Imagens"],
    "2": ["Documentos"],
    "3": ["Planilhas"],
    "4": ["Audio"],
    "5": ["Videos"],
    "6": ["Codigos"],
    "7": list(categorias.keys())  # tudo
}

escolhidas = mapa_opcoes.get(opcao, list(categorias.keys()))
# garantir que "Outros" sempre exista no conjunto final
if "Outros" not in escolhidas:
    escolhidas.append("Outros")

# 5) criar subpastas para as categorias escolhidas
for cat in escolhidas:
    subpasta = os.path.join(pasta, cat)
    if not os.path.exists(subpasta):
        os.mkdir(subpasta)

# 6) funcao para evitar sobrescrita
def nome_disponivel(caminho_destino):
    """
    Se existir um ficheiro com o mesmo nome, cria nome com sufixo (1), (2), ...
    """
    base, ext = os.path.splitext(caminho_destino)
    contador = 1
    novo = caminho_destino
    while os.path.exists(novo):
        novo = f"{base}({contador}){ext}"
        contador += 1
    return novo

# 7) contadores por categoria
contagem = {cat: 0 for cat in escolhidas}

# 8) percorrer os ficheiros e mover
for ficheiro in os.listdir(pasta):
    caminho_ficheiro = os.path.join(pasta, ficheiro)

    # ignorar diretorios e as proprias pastas de destino
    if not os.path.isfile(caminho_ficheiro):
        continue
    if ficheiro.startswith("."):  # opcional: ignorar itens ocultos
        pass

    nome, extensao = os.path.splitext(ficheiro)
    extensao = extensao.lower()

    # decidir categoria
    categoria_alvo = "Outros"
    for cat in categorias:
        if cat != "Outros" and extensao in categorias[cat]:
            categoria_alvo = cat
            break

    # se a categoria nao foi escolhida no menu, pula
    if categoria_alvo not in escolhidas and "Outros" not in escolhidas:
        continue
    if categoria_alvo not in escolhidas and categoria_alvo != "Outros":
        # por exemplo, escolheu apenas imagens, entao documentos vao para Outros se Outros foi escolhido
        if "Outros" in escolhidas:
            categoria_alvo = "Outros"
        else:
            continue

    destino_dir = os.path.join(pasta, categoria_alvo)
    destino = os.path.join(destino_dir, ficheiro)

    # evitar sobrescrever
    destino_final = nome_disponivel(destino)

    shutil.move(caminho_ficheiro, destino_final)
    contagem[categoria_alvo] = contagem.get(categoria_alvo, 0) + 1

# 9) relatorio final
print("\n=== Relatorio ===")
for cat in escolhidas:
    print(f"{cat}: {contagem.get(cat, 0)} ficheiros movidos")
print("\nConcluido")
