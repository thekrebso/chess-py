import pygame
import math

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DEFAULT_REFRESH_RATE = 60


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hello, World!")

        try:
            self.refresh_rate = pygame.display.get_current_refresh_rate()
            print(f"Current monitor refresh rate: {self.refresh_rate} Hz")
        except:
            try:
                refresh_rates = pygame.display.get_desktop_refresh_rates()
                self.refresh_rate = max(
                    refresh_rates) if refresh_rates else DEFAULT_REFRESH_RATE
                print(f"Fastest monitor refresh rate: {self.refresh_rate} Hz")
            except:
                self.refresh_rate = DEFAULT_REFRESH_RATE
                print(
                    f"Failed to get refresh rate, using default: {DEFAULT_REFRESH_RATE} Hz")

        self.font = pygame.font.Font(None, 74)
        self.font_fps = pygame.font.Font(None, 24)
        self.text = self.font.render("Hello, World!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def cleanup(self):
        pygame.quit()


class Renderer:
    def __init__(self, game: Game):
        self.game = game

    def render(self):
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(self.game.text, self.game.text_rect)
        self.render_overlay()

    def render_overlay(self):
        fps = self.game.clock.get_fps()
        fps_text = self.game.font_fps.render(
            f"{math.floor(fps)} / {self.game.refresh_rate}", True, (255, 255, 255))
        fps_text_rect = fps_text.get_rect()
        self.game.screen.blit(fps_text, fps_text_rect)


class InputHandler:
    def __init__(self, game: Game):
        self.game = game

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True


def main():
    game = Game()
    renderer = Renderer(game)
    input_handler = InputHandler(game)

    while True:
        if not input_handler.handle_input():
            game.cleanup()
            return

        renderer.render()

        pygame.display.flip()
        game.clock.tick(game.refresh_rate)


if __name__ == "__main__":
    main()
