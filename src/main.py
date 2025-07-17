import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Hello, World!")

    font = pygame.font.Font(None, 74)
    text = font.render("Hello, World!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
