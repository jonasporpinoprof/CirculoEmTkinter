import pygame
import time

# Inicializar o pygame
pygame.init()

# Configurações da janela
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Janela com Círculo e Fundo de Imagem")

# Carregar imagem de fundo
bg_image = pygame.image.load("linhas3d.png")
bg_image = pygame.transform.scale(bg_image, window_size)

# Variável do raio e posição inicial do círculo
circle_radius = 100
circle_x = 250
circle_y = 250

# Configuração de cores
circle_color = (0, 0, 255)  # Azul

# Função para diminuir o círculo e movê-lo para cima
def diminuir_e_mover_circulo():
    global circle_radius, circle_y
    if circle_radius > 0:
        circle_radius -= 5
        circle_y -= 10  # Ajuste a quantidade para controlar a velocidade do movimento para cima

# Loop principal do pygame
running = True
last_update_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    current_time = time.time()
    if current_time - last_update_time >= 1:
        diminuir_e_mover_circulo()
        last_update_time = current_time

    # Limpar a tela antes de desenhar
    screen.fill((0, 0, 0))

    # Desenhar imagem de fundo
    screen.blit(bg_image, (0, 0))

    # Desenhar o círculo
    if circle_radius > 0:
        pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a taxa de quadros
    pygame.time.delay(100)

# Finalizar o pygame
pygame.quit()
