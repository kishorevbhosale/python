# Check wheater the two given BTrees are identical or not

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        

def search_identical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is not None and tree2 is not None:
        return((tree1.data == tree2.data) and search_identical(tree1.left, tree2.left) and search_identical(tree1.right, tree2.right))
    
tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)
tree1.left.left = Node(4)

tree2 = Node(1)
tree2.left = Node(2)
tree2.right = Node(3)
tree2.left.left = Node(5)

print(search_identical(tree1, tree2))
