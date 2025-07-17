import pygame
import math
import logging
import typing

WINDOW_TITLE = "Pychess"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DEFAULT_REFRESH_RATE = 60


class Logger:
    def __init__(self):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(message)s",
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)


class FontManager:
    def __init__(self):
        self.font_sizes = {
            "h1": 96,
            "h2": 72,
            "h3": 48,
            "h4": 36,
            "h5": 24,
            "h6": 18,
            "normal": 28
        }

        self.fonts = {
            key: pygame.font.Font(None, size) for key, size in self.font_sizes.items()
        }

    def get_font(self, style: str) -> pygame.font.Font:
        return self.fonts.get(style, self.fonts["normal"])


class Game:
    def __init__(self):
        self.logger = Logger()

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        try:
            self.refresh_rate = pygame.display.get_current_refresh_rate()
            self.logger.info(
                f"Current monitor refresh rate: {self.refresh_rate} Hz")
        except:
            try:
                refresh_rates = pygame.display.get_desktop_refresh_rates()
                self.refresh_rate = max(
                    refresh_rates) if refresh_rates else DEFAULT_REFRESH_RATE
                self.logger.info(
                    f"Fastest monitor refresh rate: {self.refresh_rate} Hz")
            except:
                self.refresh_rate = DEFAULT_REFRESH_RATE
                self.logger.warning(
                    f"Failed to get refresh rate, using default: {DEFAULT_REFRESH_RATE} Hz")

        self.font_manager = FontManager()

        self.text = self.font_manager.get_font("h1").render(
            "Hello, World!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def cleanup(self):
        pygame.quit()


class Renderer:
    def __init__(self, game: Game):
        self.game = game
        self.debug_overlay = False

    def render(self):
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(self.game.text, self.game.text_rect)

        if self.debug_overlay:
            self.render_overlay()

    def render_overlay(self):
        fps = self.game.clock.get_fps()
        fps_text = self.game.font_manager.get_font("h5").render(
            f"{math.floor(fps)} / {self.game.refresh_rate}", True, (255, 255, 255))
        fps_text_rect = fps_text.get_rect()
        self.game.screen.blit(fps_text, fps_text_rect)


class InputHandler:
    def __init__(self, game: Game, renderer: Renderer):
        self.game = game
        self.renderer = renderer

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    self.renderer.debug_overlay = not self.renderer.debug_overlay
        return True


def main():
    game = Game()
    renderer = Renderer(game)
    input_handler = InputHandler(game, renderer)

    while True:
        if not input_handler.handle_input():
            game.cleanup()
            return

        renderer.render()

        pygame.display.flip()
        game.clock.tick(game.refresh_rate)


if __name__ == "__main__":
    main()
