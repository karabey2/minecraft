import pygame
import random

# Создаем игру и окно
def main():
    WIDTH = 800
    HEIGHT = 800
    BLACK = 0,0,0
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")

    # Цикл игры
    running = True
    while running:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()