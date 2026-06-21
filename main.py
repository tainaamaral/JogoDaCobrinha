import pygame
import random

pygame.init()
pygame.font.init()
fonte = pygame.font.SysFont("arial", 25, bold=True)
fonte_titulo = pygame.font.SysFont("arial", 40, bold=True)
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Jogo da Cobrinha")

cobra = [(100, 50)]
direcao = (10, 0)
comida = (300, 200)

pontos = 0
velocidade_jogo = 10


def mostrar_tela_inicio():
    esperando = True
    while esperando:
        tela.fill((0, 0, 0))

        texto_titulo = fonte_titulo.render("JOGO DA COBRINHA", True, (0, 255, 0))
        texto_instrucao = fonte.render("Pressione qualquer tecla para jogar", True, (255, 255, 255))

        # Centraliza os textos na tela
        tela.blit(texto_titulo, (600 // 2 - texto_titulo.get_width() // 2, 130))
        tela.blit(texto_instrucao, (600 // 2 - texto_instrucao.get_width() // 2, 220))

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

    # Passa a variável pontos para a função desenhar
    desenhar(pontos)
    relogio.tick(velocidade_jogo)

pygame.quit()



