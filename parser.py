import re

class SANParser:
    def __init__(self):
        self.move_pattern = re.compile(r"""
            (O-O(-O)?|                             # Castling
            [KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](=[QRBN])?[+#]?|  # Piece or pawn move
            [a-h]x[a-h][1-8](=[QRBN])?[+#]?|      # Pawn capture
            [a-h][1-8](=[QRBN])?[+#]?)            # Pawn advance
        """, re.VERBOSE)

        self.turn_pattern = re.compile(r"(\d+)\.\s*(\S+)(?:\s+(\S+))?")

    def validate_move(self, move):
        return self.move_pattern.fullmatch(move) is not None

    def parse_game(self, text):
        turns = []
        for match in self.turn_pattern.finditer(text):
            num, white, black = match.groups()
            if not self.validate_move(white):
                raise ValueError(f"Invalid white move at turn {num}: {white}")
            if black and not self.validate_move(black):
                raise ValueError(f"Invalid black move at turn {num}: {black}")
            turns.append((int(num), white, black))
        return turns