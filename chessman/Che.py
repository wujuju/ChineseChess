
from ChessPiece import ChessPiece

class Che(ChessPiece):

    def get_image_file_name(self):
            if self.is_red:
                return "images/redJu0.png"
            else:
                return "images/blackJu0.png"


    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            #print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        if (nx, ny) not in board.pieces:
            if cnt!= 0:
                #print 'blocked'
                return False
        else:
            if cnt != 0:
                #print 'cannot kill'
                return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

