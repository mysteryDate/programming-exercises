# Given a chess board of order NxM and source points (s1,s2) and destination points (d1,d2),
# Your task to find min number of moves required by the Knight to go to the destination cell.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases.
# Then T test cases follow. Each test case contains two lines.
# The first line of each test case contains two space separated integers N and M.
# Then in the next line are four space separated values s1, s2 and d1, d2.
#
# Output:
# For each test case in a new line print the min no of moves required by the knight to go to
# the destination from the source. If no such move is possible print -1.

# Example:
# Input:
# 2
# 4 7
# 2 6 2 4
# 7 13
# 2 8 3 4
# Output:
# 2
# 3


def make_board(width, height):
    board = {}
    jumps = [(x, y) for x in [-2, 2] for y in [-1, 1]] + [(x, y) for x in [-1, 1] for y in [-2, 2]]
    for x in range(width):
        for y in range(height):
            board[(x, y)] = []
            for jx, jy in jumps:
                newx, newy = x + jx, y + jy
                if newx >= 0 and newx < width and newy >= 0 and newy < height:
                    board[(x, y)].append((newx, newy))
    return board


def knightwalk(width, height, source, destination):
    board = make_board(width, height)
    squares_to_visit = [(source, 0)]
    visited = set()
    while len(squares_to_visit) > 0:
        current_square, num_jumps = squares_to_visit.pop(0)
        visited.add(current_square)
        if current_square == destination:
            return num_jumps
        for new_square in board[current_square]:
            if new_square not in visited:
                squares_to_visit.append((new_square, num_jumps + 1))
    return -1


# for _ in range(int(input())):
#     width, height = [int(x) for x in input().split(' ')]
#     s1, s2, d1, d2 = [int(x) for x in input().split(' ')]
#     num_steps = knightwalk(width, height, (s1 - 1, s2 - 1), (d1 - 1, d2 - 1))
#     print(num_steps)


i1 = "3 11"
i2 = "3 11 2 11"
w, h = [int(x) for x in i1.split(" ")]
s1, s2, d1, d2 = [int(x) for x in i2.split(" ")]
num_steps = knightwalk(w, h, (s1, s2), (d1, d2))
print(num_steps)