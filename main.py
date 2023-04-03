import pygame


WINDOW_HEIGHT = 720
WINDOW_WIDTH = 720
SCREEN = pygame.display.set_mode((720, 720))

def main():
    pygame.init()

    clock = pygame.time.Clock
    running = True

    while running:


        SCREEN.fill(pygame.Color("#282828"))

        pygame.draw.rect(SCREEN, "blue", pygame.Rect(30, 30, 100, 40))
        font = pygame.font.SysFont(None, 32)
        start_button = font.render('Start', True, "red")
        SCREEN.blit(start_button, (52, 40))

        rects = draw_grid()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()  # get the mouse pos
                for rect in rects:
                    if rect.collidepoint(mouse_pos):  # checking if the mouse_pos is inside the rectangle
                        print("x:" + str(rect.x) + " " + "y:" + str(rect.y))

    pygame.quit()

def draw_grid():
    rects = []
    block_size = 20
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range (0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            rects.append(pygame.draw.rect(SCREEN, pygame.Color("#e1e1e1"), rect, 1))

    return rects

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
