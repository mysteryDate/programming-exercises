# Given N * M string array of O's and X's
# Return the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

# Example:
# Input:
# 2
# 4 7
# OOOOXXO OXOXOOX XXXXOXO OXXXOOO
# 10 3
# XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO
# Output:
# 4
# 6


def get_shapes(board):
    jumps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    num_shapes = 0
    visited = set()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if (x, y) not in visited and board[x][y] == "X":
                to_visit = [(x, y)]
                while len(to_visit) > 0:
                    x1, y1 = to_visit.pop(0)
                    visited.add((x1, y1))
                    for xn, yn in [(x1 + x2, y1 + y2) for x2, y2 in jumps]:
                        if xn >= 0 and xn < len(board) and yn >= 0 and yn < len(board[x]):
                            if (xn, yn) not in visited:
                                if board[xn][yn] == "X":
                                    to_visit.append((xn, yn))
                num_shapes += 1
    return num_shapes

i1 = "4 7"
i2 = "XXO OOX OXO OOO XOX XOX OXO XXO XXX OOX "
board = i2.split(" ")
board = [list(x) for x in board if x != '']
s = get_shapes(board)
print(s)
