class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def createnode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createnode(data)
        if ch == 'L':
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return True is Tree is SumTree else return False
def get_tree_sum(root):
    if root is None:
        return 0
    return get_tree_sum(root.left) + root.data + get_tree_sum(root.right)


def isSumTree(root):
    if root is None:
        return True
    left_sum = get_tree_sum(root.left)
    right_sum = get_tree_sum(root.right)
    branch_sum = left_sum + right_sum
    if branch_sum == root.data or branch_sum == 0:
        if isSumTree(root.left) and isSumTree(root.right):
            return True
        return False
    return False

inN = 2
inT = "3 1 L 3 2 R"
# Driver Program
if __name__ == '__main__':
    n = int(inN)
    arr = inT.strip().split()
    if n == 0:
        print(1)
    tree = Tree()
    lis = []
    root = None
    root = tree.insert(root, int(arr[0]), 'L')
    lis.append(root)
    k = 0
    for j in range(n):
        ptr = None
        ptr = tree.search(lis, int(arr[k]))
        lis.append(tree.insert(ptr, int(arr[k + 1]), arr[k + 2]))
        k += 3
    if isSumTree(root):
        print(1)
    else:
        print(0)
# Contributed by: Harshit Sidhwa