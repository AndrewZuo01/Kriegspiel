import pygame

# Board dimensions
ROWS = 10
COLS = 5

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Square dimensions
SQUARE_SIZE = 80

# Initialize Pygame
pygame.init()

# Set up the display
window_width = COLS * SQUARE_SIZE
window_height = ROWS * SQUARE_SIZE
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Chinese Military Chess")

# draw board and piece image
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE


            color = WHITE
            # default board
            pygame.draw.rect(window, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            piece = board[row][col]
            # if piece exist get image
            if piece:
                image = piece.image
                window.blit(image, (x, y))
# get indice from cursor
def get_indices_from_cursor(cursor_x, cursor_y):
    row = cursor_y // SQUARE_SIZE
    col = cursor_x // SQUARE_SIZE
    return row, col

# following are chess piece
class ChessPiece:
    def __init__(self, rank, owner):
        self.rank = rank
        self.owner = owner
        self.image = pygame.image.load("flag.png")
        self.is_hidden = True  # Whether the piece is hidden (covered by the fog of war)

    def reveal(self):
        self.is_hidden = False

class Flag(ChessPiece):
    def __init__(self, owner):
        super().__init__(1, owner)

class Soldier(ChessPiece):
    def __init__(self, owner):
        super().__init__(2, owner)
        self.image = pygame.image.load("soldier.png")
# chess board, check valid move, move pieve, place and remove pieces
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

class ChineseMilitaryChess:
    def __init__(self):
        self.board = ChessBoard()
        self.player1_pieces = []
        self.player2_pieces = []

    def initialize_board(self):
        # Place player 1's pieces
        player1_pieces = [
            Flag(1),
            Soldier(1),
            Soldier(1),
            Soldier(1),
            Soldier(1),
            Soldier(1),
            Soldier(1),
        ]
        self.player1_pieces = player1_pieces

        # Place player 2's pieces
        player2_pieces = [
            Flag(2),
            Soldier(2),
            Soldier(2),
            Soldier(2),
            Soldier(2),

        ]
        self.player2_pieces = player2_pieces

        # Place the pieces on the board without player
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in [(3, 0), (3, 8), (4, 0), (4, 8)]:
                    if row < 5 and player1_pieces:
                        piece = player1_pieces.pop()
                    elif row >= 5 and player2_pieces:
                        piece = player2_pieces.pop()
                    else:
                        piece = None
                    self.board.place_piece(piece, row, col)
                    
    def play(self):
        # Game loop
        selected_piece = None  
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                #     mouse_x, mouse_y = pygame.mouse.get_pos()
                #     row, col = get_indices_from_cursor(mouse_x, mouse_y)

                #     # Check if a piece is already selected and attempt to move it
                #     if selected_piece:
                #         if self.board.is_valid_move(selected_piece.row, selected_piece.col, row, col):
                #             self.board.move_piece(selected_piece.row, selected_piece.col, row, col)
                #         selected_piece = None  # Deselect the piece

                #     else:
                #         # Check if a piece is present at the clicked position
                #         piece = self.board.board[row][col]
                #         if piece:
                #             selected_piece = piece  # Select the piece


            # Clear the window
            window.fill(BLACK)

            # Draw the board
            draw_board(self.board.board)
            
            # Update the display
            pygame.display.flip()

        # Quit the game
        pygame.quit()

# Example usage
game = ChineseMilitaryChess()
game.initialize_board()
game.play()


