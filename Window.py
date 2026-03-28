import pygame

pygame.init()

WINDOW_W, WINDOW_H = 500, 500
FPS = 60

screen = pygame.display.set_mode((WINDOW_W,WINDOW_H))
clk = pygame.time.Clock()
running = True
lose = False


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((180,180,180))
    clk.tick(FPS)
    pygame.display.flip()
pygame.quit()