from enum import Enum


class Piece:
    class Type(Enum):
        PAWN = 0
        KNIGHT = 1
        BISHOP = 2
        ROOK = 3
        QUEEN = 4
        KING = 5

    class Color(Enum):
        WHITE = 0
        BLACK = 1

    def __init__(self, color: Color, type: Type):
        self.color = color
        self.type = type
        self.has_moved = False

    def __repr__(self):
        return f"{self.color.name} {self.type.name}"
