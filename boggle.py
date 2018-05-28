# Given a dictionary, a method to do lookup in dictionary
# and a M x N board where every cell has one character.
# Find all possible words that can be formed by a sequence of adjacent characters.
# Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

# Example:
# Input:
# 1
# 4
# GEEKS FOR QUIZ GO
# 3 3
# G I Z U E K Q S E
#
# Output:
# GEEKS QUIZ


class GraphNode:
    def __init__(self, letter):
        self.letter = letter
        self.edges = set()

    def add_edge(self, node):
        self.edges.add(node)

    def __repr__(self):
        if len(self.edges) == 0:
            return "{}".format(self.letter)
        return "{l} -> {e}".format(l=self.letter, e=[x.letter for x in self.edges])


class DictNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = set()

    def add_child(self, node):
        self.children.add(node)

    def get_child_with_letter(self, letter):
        for c in self.children:
            if c.letter == letter:
                return c
        return -1

    def __repr__(self):
        if len(self.children) == 0:
            return "{}".format(self.letter)
        return "{l} -> {c}".format(l=self.letter, c=self.children)


def make_board_graph(board_letters, width, height):
    board = [[''] * width for _ in range(height)]
    nodes = []
    for y in range(height):
        for x in range(width):
            board[y][x] = GraphNode(board_letters.pop(0))
            nodes.append(board[y][x])
    for y in range(len(board)):
        for x in range(len(board[0])):
            step_range = [-1, 0, 1]
            for newX, newY in [(x + x1, y + y1) for x1 in step_range for y1 in step_range]:
                if newX >= 0 and newY >= 0:
                    if newX < width and newY < height:
                        if not (newX == x and newY == y):
                            board[y][x].edges.add(board[newY][newX])
    head = GraphNode('')
    for n in nodes:
        head.edges.add(n)
    return head


def make_prefix_dict(word_list):
    prefix_dict = DictNode("")
    for word in word_list:
        current_node = prefix_dict
        for letter in word:
            already_there = False
            for child in current_node.children:
                if child.letter == letter:
                    current_node = child
                    already_there = True
                    break
            if not already_there:
                new_node = DictNode(letter)
                current_node.children.add(new_node)
                current_node = new_node
        current_node.children.add(DictNode("."))
    return prefix_dict


def get_all_boggle_words(dictionary, board_letters, w, h):
    prefix_dict = make_prefix_dict(dictionary)
    board_graph = make_board_graph(board_letters, w, h)
    result_words = set()
    nodes_to_visit = [(board_graph, prefix_dict, "", set())]
    while len(nodes_to_visit) > 0:
        current_node, dict_node, word, visited_nodes = nodes_to_visit.pop(0)
        new_visited = set(visited_nodes)
        new_visited.add(current_node)
        for board_child in current_node.edges:
            if board_child in new_visited:
                continue
            lc = dict_node.get_child_with_letter(board_child.letter)
            if lc != -1:
                nodes_to_visit.append((board_child, lc, word + board_child.letter, new_visited))
        if dict_node.get_child_with_letter(".") != -1:
            result_words.add(word)
    sorted_words = sorted([w for w in result_words])
    return sorted_words


ii = [["4", "GEEKS FOR QUIZ GO", "3 3", "G I Z U E K Q S E"]]
ii2 = [["6","b edc ddd cc ccb ffb","5 2","d d c c b f d d c d"]]
ii3 = [["6", "dfd ded fd e dec df", "4 2", "f f d e f b b e"]]

# for _ in range(int(input())):
#     num_words = int(input())
#     words = input().split(" ")
#     width, height = (int(x) for x in input().split(" ") if x != '')
#     board_letters = input().split(" ")
#     words = get_all_boggle_words(words, board_letters, width, height)

for input_entry in ii3:
    num_words = int(input_entry[0])
    di = input_entry[1].split(" ")
    width, height = (int(x) for x in input_entry[2].split(" ") if x != '')
    bl = input_entry[3].split(" ")
    words = get_all_boggle_words(di, bl, width, height)
    print(words)
