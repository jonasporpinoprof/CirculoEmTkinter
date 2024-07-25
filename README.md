# Explicação:
## Limpar a tela:
screen.fill((0, 0, 0)): Limpa a tela preenchendo-a com a cor preta antes de desenhar a imagem de fundo e o círculo. Isso remove os rastros do círculo anterior.

## Manter a ordem de desenho:
A imagem de fundo é desenhada primeiro (screen.blit(bg_image, (0, 0))), seguida pelo círculo (pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)). Isso garante que o círculo seja desenhado sobre a imagem de fundo.

## Atualização da tela:
pygame.display.flip(): Atualiza a tela com o novo desenho.
Com essas alterações, o rastro do círculo é removido e a tela é redesenhada a cada atualização, garantindo que apenas o círculo atual seja visível.






