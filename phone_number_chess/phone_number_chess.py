# --------------------------------------------------
class Piece:
    name = ''       # string (ex: 'knight')
    board = [[]]    # list of lists (ex: [[1,2,3], [4,5,6]])
    num_rows = 0    # int (ex: 2)
    num_cols = 0    # int (ex: 3)
    routes = dict((digit, []) for digit in range(0, 10))   # dict (ex: {1: [6, 4]})

    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])
        self.build_routes()
        
    def build_routes(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if board[i][j].isdigit():
                    start_key = int(board[i][j])
                    self.routes[start_key] = self.valid_routes(i, j)

class Knight(Piece):  
    def __init__(self, board):
        Piece.__init__(self, name='knight', board=board)
    
    def valid_routes(self, i, j):
        valid_routes = []
        moves = [[+1 ,+2], [+2, +1],
                 [-1 ,+2], [-2, +1],
                 [+1, -2], [+2, -1],
                 [-1, -2], [-2, -1]]
        for move in moves:
            if i+move[0] >= 0 and i+move[0] < self.num_rows and \
               j+move[1] >= 0 and j+move[1] < self.num_cols and \
               self.board[i+move[0]][j+move[1]].isdigit():
                end_key = int(self.board[i+move[0]][j+move[1]])
                valid_routes.append(end_key)
        return valid_routes

class Bishop(Piece):
    def __init__(self, board):
        Piece.__init__(self, name='bishop', board=board)
    
    def valid_routes(self, i, j):
        valid_routes = []
        directions = [[-1, -1], [-1, +1],
                      [+1, -1], [+1, +1]]
        for direction in directions:
            dir_i, dir_j = direction
            curr_i = i; curr_j = j
            while curr_i + dir_i >= 0 and curr_i + dir_i < self.num_rows and \
                  curr_j + dir_j >= 0 and curr_j + dir_j < self.num_cols and \
                  self.board[curr_i + dir_i][curr_j + dir_j].isdigit():
                end_key = int(self.board[curr_i + dir_i][curr_j + dir_j])
                valid_routes.append(end_key)
                curr_i += dir_i; curr_j += dir_j
        return valid_routes

# --------------------------------------------------
# Read in
# Make sure to convert digits to ints, will probably be useful for indexing
piece_name = 'knight'
number_length = 7
starting_digits = '2 3 4 5 6 7 8 9'
starting_digits = starting_digits.split(' ')
starting_digits = [int(i) for i in starting_digits]
num_rows = 4
num_cols = 3
board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9'],
         ['*', '0', '#']]
valid_digits = []
for row in board:
    valid_digits += [int(i) for i in row if i.isdigit()]

# Build valid routes {start_digit : end_digits_list}
# Use isdigit() to check if is digit
if piece_name == 'knight':   piece = Knight(board)
elif piece_name == 'bishop': piece = Bishop(board)
print(piece.routes)

# ways[i][j] = number of phone numbers with length i+1 that end in number j
num_numbers = [[0 for j in range(0, 10)] for i in range(number_length)]

# Fill in base case for starting_digits input; zero valid numbers for non-valid starting digits
num_numbers[0] = [1 if i in starting_digits and i in valid_digits else 0
                  for i in range(len(num_numbers[0]))]

# Fill in table
for i in range(1, number_length):   # Iterate across lengths from 2 to number_length
    for j in range(0, 10):          # Iterate across potential ending digits
        for k in piece.routes[j]:   # Iterate across starting digits, given the ending digit
            num_numbers[i][j] += num_numbers[i-1][k]   # Add in the numbers of ways coming from digit k
print(num_numbers)

# Sum up all possible numbers with length = number_length
print(sum(num_numbers[number_length-1]))