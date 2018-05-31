# Implement a function to check if a tree is balanced For the purposes of this question,
# a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
# from the root by more than one


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def __repr__(self):
        if self.is_leaf():
            return "{}".format(self.value)
        return "{l} <-- {v} --> {r}".format(v=self.value, l=self.left, r=self.right)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value, current_node=None):
        if self.root is None:
            self.root = TreeNode(value)
            return
        if current_node is None:
            current_node = self.root
        if value <= current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self.insert(value, current_node=current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self.insert(value, current_node=current_node.right)

    def max_depth(self, node):
        if node is None:
            return 0
        return 1 + max(max_depth(node.left), max_depth(node.right))

    def get_row(self, row, current_node, current_depth=0):
        if current_node is None:
            return [" "] if current_depth == row else []
        if current_depth == row:
            return [current_node.value]
        return self.get_row(row, current_node.left, current_depth + 1) + self.get_row(row, current_node.right, current_depth + 1)

    def __repr__(self):
        md = self.max_depth(self.root)
        result = ""
        for i in range(md):
            result += " ".join([str(x) for x in self.get_row(i, self.root)])
            result += "\n"
        return result


def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    return False


def is_balanced(root):
    if is_leaf(root):
        return True
    if root.left is None:
        if is_leaf(root.right):
            return True
        return False
    if root.right is None:
        if is_leaf(root.left):
            return True
        return False
    if is_balanced(root.left) and is_balanced(root.right):
        return True
    return False


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root):
    if root is None:
        return 0
    return 1 + min(min_depth(root.left), min_depth(root.right))


def book_is_balanced(root):
    print(max_depth(root))
    print(min_depth(root))
    if max_depth(root) - min_depth(root) > 1:
        return False
    return True


import random
# values = [random.randint(0, 9) for _ in range(3)]
values = [5, 4, 6, 3, 5, 5, 7]
tree = Tree()
for x in values:
    tree.insert(x)
print(tree)
print(is_balanced(tree.root))
print(book_is_balanced(tree.root))
