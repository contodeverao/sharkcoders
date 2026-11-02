import pygame
import random
import sys
import os

# janela
LARGURA = 480
ALTURA = 640
FPS = 60

# cores
BRANCO = (255, 255, 255)

# assets
ASSETS = "assets"

def carregar_img(nome, tamanho=None):
    caminho = os.path.join(ASSETS, nome)
    img = pygame.image.load(caminho).convert_alpha()
    if tamanho:
        img = pygame.transform.smoothscale(img, tamanho)
    return img

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carregar_img("shark.png", (96, 96))
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 20

    def update(self):
        return


def main():
    pygame.init()
    pygame.display.set_caption("Shark Dodger")
    ecran = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()

    # fundo
    background = carregar_img("background.jpeg", (LARGURA, ALTURA))

    todos = pygame.sprite.Group()

    jogador = Jogador()
    todos.add(jogador)

    pontuacao = 0
    vidas = 3
    tempo = 0
    dif_timer = 0

    a_correr = True
    while a_correr:
        dt = relogio.tick(FPS) / 1000
        tempo += dt
        dif_timer += dt

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                a_correr = False

        todos.update()

        # desenhar
        ecran.blit(background, (0, 0))
        todos.draw(ecran)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
