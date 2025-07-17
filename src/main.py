import pygame
import math

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DEFAULT_REFRESH_RATE = 60


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hello, World!")

    try:
        refresh_rate = pygame.display.get_current_refresh_rate()
        print(f"Current monitor refresh rate: {refresh_rate} Hz")
    except:
        try:
            refresh_rates = pygame.display.get_desktop_refresh_rates()
            refresh_rate = max(refresh_rates) if refresh_rates else DEFAULT_REFRESH_RATE
            print(f"Fastest monitor refresh rate: {refresh_rate} Hz")
        except:
            refresh_rate = DEFAULT_REFRESH_RATE
            print(
                f"Failed to get refresh rate, using default: {DEFAULT_REFRESH_RATE} Hz")

    font = pygame.font.Font(None, 74)
    font_fps = pygame.font.Font(None, 24)
    text = font.render("Hello, World!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        fps = clock.get_fps()
        fps_text = font_fps.render(
            f"{math.floor(fps)} / {refresh_rate}", True, (255, 255, 255))
        fps_text_rect = fps_text.get_rect()

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        screen.blit(fps_text, fps_text_rect)

        pygame.display.flip()
        clock.tick(refresh_rate)


if __name__ == "__main__":
    main()
