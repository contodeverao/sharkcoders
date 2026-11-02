import os
import shutil

print("=== Organizador de Ficheiros ===")

# 1. Perguntar a pasta onde estão os ficheiros
pasta = input("Digite o caminho da pasta que deseja organizar: ").strip().strip('"')


# 2. Definir categorias (extensões → nome da subpasta)
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Áudio": [".mp3", ".wav"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Outros": []
}
# 3. Criar subpastas se não existirem
for categoria in categorias:
    caminho_subpasta = os.path.join(pasta, categoria)
    if not os.path.exists(caminho_subpasta):
        os.mkdir(caminho_subpasta)

# 4. Ler ficheiros da pasta
for ficheiro in os.listdir(pasta):
    caminho_ficheiro = os.path.join(pasta, ficheiro)
    if os.path.isfile(caminho_ficheiro):
        nome, extensao = os.path.splitext(ficheiro)

        # Verificar categoria do ficheiro
        movido = False
        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                shutil.move(caminho_ficheiro, os.path.join(pasta, categoria, ficheiro))
                movido = True
                break
        # Se não estiver em nenhuma categoria, vai para "Outros"
        if not movido:
            shutil.move(caminho_ficheiro, os.path.join(pasta, "Outros", ficheiro))

print("Organização concluída!")


