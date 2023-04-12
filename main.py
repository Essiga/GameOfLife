import pygame
import pygame_menu
import numpy as np

# WINDOW_HEIGHT = 720
# WINDOW_WIDTH = 720
# SCREEN = pygame.display.set_mode((720, 720))
# Define settings
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
ROWS, COLS = 25, 25
SPEED = 20
CYCLE_COUNT = 0
MAX_CYCLE = None

BG_COLOR = (128, 128, 128)
LIVE_COLOR = (255, 0, 0)
DEAD_COLOR = (255, 255, 255)

# Initialize the Pygame library and set up the screen
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    open_main_menu()

    pygame.quit()


def edit_grid(grid=None):
    clock = pygame.time.Clock
    screen = pygame.display.set_mode((500, 550))

    if grid is None:
        grid = np.zeros((ROWS, COLS))

    running = True

    while running:

        SCREEN.fill(pygame.Color("#282828"))

        font = pygame.font.SysFont(None, 24)
        start_display = font.render('Press SPACE to start', True, (255, 0, 0))

        rects = draw_grid(grid)
        SCREEN.blit(start_display, (20, 520))
        pygame.display.flip()

        state = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                grid = handle_mouse_click(grid)
            elif state[pygame.K_SPACE]:
                print("space pressed :)))))")
            elif state[pygame.K_ESCAPE]:
                open_pause_menu()


def open_pause_menu():
    screen = pygame.display.set_mode((500, 550))

    pause_menu = pygame_menu.Menu(title='Paused', theme=pygame_menu.themes.THEME_DARK, height=550, width=500)
    pause_menu.add.button("Resume")
    pause_menu.mainloop(screen)



def open_main_menu():
    screen = pygame.display.set_mode((500, 500))
    global CYCLE_COUNT
    CYCLE_COUNT = 0

    freeplay_menu = pygame_menu.Menu(title='Settings', theme=pygame_menu.themes.THEME_DARK, height=500, width=500)
    # freeplay_menu.add.range_slider('Speed', SPEED, (1, 100), 1, onchange=set_delay, value_format=lambda x: str(int(x)))
    # freeplay_menu.add.text_input('Cell Size: ', default=str(CELL_SIZE), input_type=pygame_menu.locals.INPUT_INT, onchange=set_cell_size)
    # freeplay_menu.add.text_input('Rows: ', default=str(ROWS), input_type=pygame_menu.locals.INPUT_INT, onchange=set_rows)
    # freeplay_menu.add.text_input('Columns: ', default=str(COLS), input_type=pygame_menu.locals.INPUT_INT,onchange=set_cols)
    freeplay_menu.add.button('Play', edit_grid)

    main_menu = pygame_menu.Menu(title='Game of Life', theme=pygame_menu.themes.THEME_DARK, height=500, width=500)
    main_menu.add.button('Freeplay', main_menu._open, freeplay_menu)
    # main_menu.add.button('Random', open_random_menu, main_menu)
    # main_menu.add.button('Load', load_game)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    main_menu.mainloop(screen)


def draw_grid(grid):
    rects = []

    for row in range(ROWS):
        for col in range(COLS):
            color = LIVE_COLOR if grid[row, col] else DEAD_COLOR
            rect = pygame.Rect(row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[row, col]:
                rects.append(pygame.draw.rect(SCREEN, color, rect))
            else:
                rects.append(pygame.draw.rect(SCREEN, color, rect, 1))


def handle_mouse_click(grid):
    """
    Returns new grid after handling a mouse click event, which toggles the state of the cell clicked on.

    Parameter
    ---------
    grid : ndarray
        2D array containing all individual cells.

    Returns
    -------
    ndarray
        Changed grid.
    """
    mouse_pos = pygame.mouse.get_pos()
    col = mouse_pos[1] // CELL_SIZE
    row = mouse_pos[0] // CELL_SIZE
    grid[row, col] = 1 - grid[row, col]
    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
