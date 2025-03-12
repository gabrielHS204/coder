import pygame

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Raquetes
player = pygame.Rect(30, altura//2 - 60, 10, 120)
maquina = pygame.Rect(largura - 40, altura//2 - 60, 10, 120)

# Bola
bola = pygame.Rect(largura//2 - 15, altura//2 - 15, 30, 30)

# Velocidades
velocidadePlayer = 10
velocidadeMaquina = 7
movimentoPlayer = 0
velocidadeBola_X = 7
velocidadeBola_Y = 7

# FPS padrão
fps_atual = 60  # Começa com 60 FPS
fps_opcoes = [30, 60, 120]  # Opções disponíveis
indice_fps = 1  # Posição atual no array

# Pontuação
pontos_player = 0
pontos_maquina = 0


def mover_player():
    global movimentoPlayer, fps_atual, indice_fps

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                movimentoPlayer = -velocidadePlayer
            elif evento.key == pygame.K_DOWN:
                movimentoPlayer = velocidadePlayer
            elif evento.key == pygame.K_0:  # Troca o FPS ao pressionar "0"
                indice_fps = (indice_fps + 1) % len(fps_opcoes)
                fps_atual = fps_opcoes[indice_fps]
                print(f"FPS alterado para: {fps_atual}")

        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_UP, pygame.K_DOWN]:
                movimentoPlayer = 0

    player.y += movimentoPlayer
    if player.top <= 0:
        player.top = 0
    if player.bottom >= altura:
        player.bottom = altura


def mover_bola():
    global velocidadeBola_X, velocidadeBola_Y, pontos_player, pontos_maquina

    bola.x += velocidadeBola_X
    bola.y += velocidadeBola_Y

    # Colisão com as bordas superior e inferior
    if bola.top <= 0 or bola.bottom >= altura:
        velocidadeBola_Y *= -1

    # Pontuação: Se a bola sai da tela pelos lados
    if bola.left <= 0:
        pontos_maquina += 1
        reiniciar_bola()
    elif bola.right >= largura:
        pontos_player += 1
        reiniciar_bola()


def colisao_raquete():
    global velocidadeBola_X
    if bola.colliderect(player) or bola.colliderect(maquina):
        velocidadeBola_X *= -1


def mover_maquina():
    if maquina.centery < bola.centery:
        maquina.y += velocidadeMaquina
    elif maquina.centery > bola.centery:
        maquina.y -= velocidadeMaquina
    # Limita a raquete da máquina para não sair da tela
    if maquina.top <= 0:
        maquina.top = 0
    if maquina.bottom >= altura:
        maquina.bottom = altura


def cria_placar():
    fonte = pygame.font.SysFont("Arial", 30)
    texto_jogador = fonte.render(str(pontos_player), True, branco)
    texto_pc = fonte.render(str(pontos_maquina), True, branco)
    texto_fps = fonte.render(f"FPS: {fps_atual}", True, branco)  # Mostra o FPS na tela
    
    tela.blit(texto_jogador, (largura//4, 20))
    tela.blit(texto_pc, (largura - largura//4 - texto_pc.get_width(), 20))
    tela.blit(texto_fps, (largura//2 - 40, 20))  # Exibe o FPS no meio da tela


def reiniciar_bola():
    global velocidadeBola_X, velocidadeBola_Y
    bola.x = largura // 2 - 15
    bola.y = altura // 2 - 15
    velocidadeBola_X *= -1


# Loop principal do jogo
clock = pygame.time.Clock()
rodando = True
while rodando:
    tela.fill(preto)  # Limpa a tela

    mover_player()
    mover_bola()
    colisao_raquete()
    mover_maquina()
    
    cria_placar()

    # Desenha os elementos
    pygame.draw.rect(tela, branco, player)
    pygame.draw.rect(tela, branco, maquina)
    pygame.draw.ellipse(tela, branco, bola)

    pygame.display.update()
    clock.tick(fps_atual)  # Controla o FPS dinamicamente
