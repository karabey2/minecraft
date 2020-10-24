import pygame
import random
# Создаем игру и окно
def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Обновление

        # Рендеринг
        screen.fill(BLACK)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()