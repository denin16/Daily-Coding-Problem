"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.is_unival = False

univalStrubtreeCount = 0
def depthFirstSearch(node):
    stack = []
    stack.append(node)

    while(len(stack) != 0):
        node = stack.pop(len(stack)-1)

        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
        
        print(node.value, node.is_unival)
        
        global univalStrubtreeCount
        if node.is_unival:
            univalStrubtreeCount += 1
        

def markUnivalSubtrees(node):
    
    if node == None:
        return

    if node.left == None and node.right == None: # leaf node (has no subtree)
        node.is_unival = True

    else: # not a lead node

        if node.left != None and node.right == None: # has left subtree
            node.left = markUnivalSubtrees(node.left)
            if node.left.is_unival == True and node.value == node.left.value:
                node.is_unival = True

        elif node.left == None and node.right != None: # has right subtree
            node.right = markUnivalSubtrees(node.right)
            if node.right.is_unival == True and node.value == node.right.value:
                node.is_unival = True

        else: # has both left and right subtree
            node.left = markUnivalSubtrees(node.left)
            node.right = markUnivalSubtrees(node.right)
            if (node.left.is_unival and node.right.is_unival) and (node.left.value == node.value and node.right.value == node.value):
                node.is_unival = True

    return node


if __name__ == "__main__":

    # Constructing the Graph
    node = Node(0)
    node.left = Node(1)
    node.right = Node(0)
    node.right.left = Node(1)
    node.right.right = Node(0)
    node.right.left.left = Node(1)
    node.right.left.right = Node(1)

    # Before marking unival Trees
    print("Before applying markings : ")
    depthFirstSearch(node)
    print("-------------")
    
    # Applying markings
    node = markUnivalSubtrees(node)

    # After applying markings
    print("After applying markings : ")
    depthFirstSearch(node)
    print("-------------")

    print("Number of Unival Subtrees are : ", univalStrubtreeCount)



