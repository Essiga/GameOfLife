import pygame


WINDOW_HEIGHT = 720
WINDOW_WIDTH = 720
SCREEN = pygame.display.set_mode((720, 720))

def main():
    pygame.init()

    clock = pygame.time.Clock
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill("black")

        pygame.draw.rect(SCREEN, "blue", pygame.Rect(30, 30, 100, 40))
        font = pygame.font.SysFont(None, 32)
        start_button = font.render('Start', True, "red")
        SCREEN.blit(start_button, (52, 40))

        draw_grid()

        pygame.display.flip()

    pygame.quit()

def draw_grid():
    block_size = 20
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range (0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, "white", rect, 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
