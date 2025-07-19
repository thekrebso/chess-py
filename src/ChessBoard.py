from ChessPiece import Piece
from Types import Grid
from typing import Optional

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
DEFAULT_FEN_STRING = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
FEN_STRING_NEXT_ROW = "/"
CHAR_TO_PIECE = {
    "K": (Piece.Color.WHITE, Piece.Type.KING),
    "Q": (Piece.Color.WHITE, Piece.Type.QUEEN),
    "R": (Piece.Color.WHITE, Piece.Type.ROOK),
    "B": (Piece.Color.WHITE, Piece.Type.BISHOP),
    "N": (Piece.Color.WHITE, Piece.Type.KNIGHT),
    "P": (Piece.Color.WHITE, Piece.Type.PAWN),
    "k": (Piece.Color.BLACK, Piece.Type.KING),
    "q": (Piece.Color.BLACK, Piece.Type.QUEEN),
    "r": (Piece.Color.BLACK, Piece.Type.ROOK),
    "b": (Piece.Color.BLACK, Piece.Type.BISHOP),
    "n": (Piece.Color.BLACK, Piece.Type.KNIGHT),
    "p": (Piece.Color.BLACK, Piece.Type.PAWN),
}
PIECE_TO_CHAR = {
    (Piece.Color.WHITE, Piece.Type.KING): "K",
    (Piece.Color.WHITE, Piece.Type.QUEEN): "Q",
    (Piece.Color.WHITE, Piece.Type.ROOK): "R",
    (Piece.Color.WHITE, Piece.Type.BISHOP): "B",
    (Piece.Color.WHITE, Piece.Type.KNIGHT): "K",
    (Piece.Color.WHITE, Piece.Type.PAWN): "P",
    (Piece.Color.BLACK, Piece.Type.KING): "k",
    (Piece.Color.BLACK, Piece.Type.QUEEN): "q",
    (Piece.Color.BLACK, Piece.Type.ROOK): "r",
    (Piece.Color.BLACK, Piece.Type.BISHOP): "b",
    (Piece.Color.BLACK, Piece.Type.KNIGHT): "k",
    (Piece.Color.BLACK, Piece.Type.PAWN): "p",
}


class Board:
    def __init__(self, fen_string: str = DEFAULT_FEN_STRING):
        self.board: Grid[Optional[Piece]] = []
        for _ in range(BOARD_HEIGHT):
            self.board.append([None] * BOARD_WIDTH)
        self.set_pieces(fen_string)

    def set_pieces(self, fen_string: str):
        x, y = 0, 0

        for c in fen_string:
            if c == FEN_STRING_NEXT_ROW:
                x += 1
                y = 0
            elif c.isdigit():
                y += int(c)
            elif c in CHAR_TO_PIECE:
                if not (x < BOARD_HEIGHT and y < BOARD_WIDTH):
                    raise ValueError(
                        "invalid FEN string: board dimensions exceeded")
                color, type = CHAR_TO_PIECE[c]
                self.board[x][y] = Piece(color, type)
                y += 1

    def move_piece(self, x: int, y: int):
        raise NotImplementedError()

    def get_valid_moves(self):
        raise NotImplementedError()

    def __repr__(self):
        result = ""

        for row in self.board:
            for piece in row:
                if piece is None:
                    result += " "
                else:
                    result += PIECE_TO_CHAR[(piece.color, piece.type)]
            result += "\n"

        return result
