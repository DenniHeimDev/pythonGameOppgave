import pygame
import color

gameColor = color.color()

FPS = 60
clock = pygame.time.Clock()

def main():
    pygame.init()
    
    window()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(FPS)


def window():
    # setup window 
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Window")


if __name__ == '__main__':
    main()