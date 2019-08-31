# board.py

board = [[i] * 8 for i in range(9)]
board[7][7] == -1

for row in board:
    print((' %2i' * 8) % tuple(row))