"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""

"""
                        1
                       / \
                     2     3
                    /  \    
                   4    5 
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Function to write to a file
def writeToFile(valueArr, fileName):
    valueArr = map(str, valueArr)
    strToWrite = "|".join(valueArr)
    with open(fileName+'.txt', 'w') as serializedFile:
        serializedFile.write(strToWrite)
    
# Function to read from a file
def readFromFile(fileName):
    strRead = ""
    with open(fileName+'.txt', 'r') as deserializedFile:
        strRead = deserializedFile.read()
        valueArr = list(map(int, strRead.split("|")))
        return valueArr
        
# Preorder Traversal
def preOrderTraversal(node):
    if node is None:
        return
    
    preOrderTravList.append(node.value)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

# Inorder Traversal
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    inOrderTravList.append(node.value)
    inOrderTraversal(node.right)

    
# Tree Construction
preIndex = 0
iteration = 0
def constructTreeFromOrder(inOrdArr, preOrdArr, startIndex, endIndex):
    if startIndex > endIndex:
        return

    """  ---------  """
    global iteration
    print(iteration, startIndex, endIndex)
    iteration += 1
    

    global preIndex
    root = Node(preOrdArr[preIndex])
    preIndex += 1

    inIndex = 0
    for i in range(startIndex, endIndex+1):
        if inOrdArr[i] == root.value:
            inIndex = i
            break
    
    root.left = constructTreeFromOrder(inOrdArr, preOrdArr, startIndex, inIndex-1)
    root.right = constructTreeFromOrder(inOrdArr, preOrdArr, inIndex+1, endIndex)
    return root
    

if __name__ == '__main__':

    preOrderTravList = []
    inOrderTravList = []
    
    preOrderTraversal(root)
    inOrderTraversal(root)

    print("Pre : ", preOrderTravList)
    print("In : ", inOrderTravList)

    lenOfTravArrs = len(preOrderTravList)
    newRoot = constructTreeFromOrder(inOrderTravList, preOrderTravList, 0, lenOfTravArrs)

    preOrderTravList = []
    preOrderTraversal(newRoot)
    print("New Pre : ", preOrderTravList)


