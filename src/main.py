import pygame
import math
import logging
import typing

WINDOW_TITLE = "Pychess"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DEFAULT_REFRESH_RATE = 60
DEFAULT_LOGGING_LEVEL = logging.INFO


class Logger:
    def __init__(self):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(message)s",
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

        self.levels = [logging.DEBUG, logging.INFO]
        self.current_level_index = self.levels.index(DEFAULT_LOGGING_LEVEL)
        self.logger.setLevel(self.levels[self.current_level_index])

    def set_level(self, level_index: int):
        self.current_level_index = level_index % len(self.levels)
        self.logger.setLevel(self.levels[self.current_level_index])
        self.logger.info(
            f"Logging level set to {logging.getLevelName(self.levels[self.current_level_index])}")

    def toggle_level(self):
        self.set_level(self.current_level_index + 1)

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
            "H1": 96,
            "H2": 72,
            "H3": 48,
            "H4": 36,
            "H5": 24,
            "H6": 18,
            "NORMAL": 28
        }

        self.fonts = {
            key: pygame.font.Font(None, size) for key, size in self.font_sizes.items()
        }

    def get_font(self, style: str) -> pygame.font.Font:
        return self.fonts.get(style, self.fonts["NORMAL"])


class Game:
    def __init__(self):
        self.logger = Logger()
        self.debug_overlay = False

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

        self.text = self.font_manager.get_font("H1").render(
            "Hello, World!", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def update(self, dt: float):
        self.dt = dt

    def cleanup(self):
        pygame.quit()


class Renderer:
    def __init__(self, game: Game):
        self.game = game

    def render(self):
        self.game.screen.fill((0, 0, 0))
        self.game.screen.blit(self.game.text, self.game.text_rect)
        if self.game.debug_overlay:
            self.render_overlay()

    def render_overlay(self):
        fps = self.game.clock.get_fps()
        fps_text = self.game.font_manager.get_font("H5").render(
            f"{math.floor(fps)} / {self.game.refresh_rate}", True, (255, 255, 255))
        fps_text_rect = fps_text.get_rect()
        self.game.screen.blit(fps_text, fps_text_rect)


class InputHandler:
    def __init__(self, game: Game):
        self.game = game

    def handle_input(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    self.game.debug_overlay = not self.game.debug_overlay
                if event.key == pygame.K_F4:
                    self.game.logger.toggle_level()
        return True


def main():
    game = Game()
    renderer = Renderer(game)
    input_handler = InputHandler(game)

    while True:
        dt = game.clock.tick(game.refresh_rate)
        if not input_handler.handle_input():
            game.cleanup()
            return

        game.update(dt)
        renderer.render()
        pygame.display.flip()


if __name__ == "__main__":
    main()
