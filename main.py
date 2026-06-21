import pygame
import random

pygame.init()
pygame.font.init()
fonte = pygame.font.SysFont("arial", 25, bold=True)

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jogo da Cobrinha")

cobra = [(100, 50)]
direcao = (10, 0)
comida = (300, 200)

pontos = 0
velocidade_jogo = 15
tamanho_bloco = 20

def desenhar():
    tela.fill((0,0,0))

    for parte in cobra:
        pygame.draw.rect(tela, (0, 55, 0), (*parte, 10, 10))

    centro_x = comida[0] + tamanho_bloco // 2
    centro_y = comida[1] + tamanho_bloco // 2
    raio = tamanho_bloco // 2
    pygame.draw.circle(tela, (255, 0, 0), (comida[0] + 5, comida[1] + 5), 5)

    texto_placar = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto_placar, (10, 10))
    
    pygame.display.update()

rodando = True
relogio = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            # Só vai para cima se não estiver indo para baixo
            if evento.key == pygame.K_UP and direcao != (0, 10):
                direcao = (0, -10)
            # Só vai para baixo se não estiver indo para cima
            elif evento.key == pygame.K_DOWN and direcao != (0, -10):
                direcao = (0, 10)
            # Só vai para a esquerda se não estiver indo para a direita
            elif evento.key == pygame.K_LEFT and direcao != (10, 0):
                direcao = (-10, 0)
            # Só vai para a direita se não estiver indo para a esquerda
            elif evento.key == pygame.K_RIGHT and direcao != (-10, 0):
                direcao = (10, 0)

    nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
    cobra.insert(0, nova_cabeca)

    if nova_cabeca == comida:
        comida = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
    else:
        cobra.pop()

    if nova_cabeca in cobra[1:]:
        rodando = False

    if nova_cabeca[0] < 0 or nova_cabeca[0] >= 600:
        rodando = False

    if nova_cabeca[1] < 0 or nova_cabeca[1] >= 400:
        rodando = False

    desenhar(pontos)
    relogio.tick(velocidade_jogo)

pygame.quit()



