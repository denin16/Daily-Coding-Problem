"""
Question 24:
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants 
or ancestors are not locked.

Design a binary tree node class with the following methods:
- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should 
- lock it and return true unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 

Otherwise, it should unlock it and return true. You may augment the node to add parent pointers or any other 
property you would like. You may assume the class is used in a single-threaded program, so there is no need for 
actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""
import queue

class Node:
    # node constructor
    def __init__(self, nodeValue=None, leftNode=None, rightNode=None, parentNode=None):
        self.nodeValue = nodeValue
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.parentNode = parentNode
        self.isLocked = False

    # method to check if all ancestors are unlocked
    def areAncestorsUnlocked(self):
        if self == None: return False # node is Null
        elif self.parentNode == None: return True # parent node is Null
        else: # does have parent nodes
            nodesStack = list()
            nodesStack.append(self.parentNode)

            while len(nodesStack) > 0:
                node = nodesStack.pop()
                if node.isLocked == True:
                    return False
                if node.parentNode != None: nodesStack.append(node.parentNode)
                    
            return True
    
    # method to check if all decendants are unlocked
    def areDecendantsUnlocked(self):
        if self == None: return False # node is Null
        elif self.leftNode == None and self.rightNode == None: return False # path child nodes are null
        else:
            nodeStack = list()
            if self.leftNode != None: nodeStack.append(self.leftNode)
            if self.rightNode != None: nodeStack.append(self.rightNode)

            while len(nodeStack) > 0:
                node = nodeStack.pop()
                if node.isLocked == True:
                    return False
                if node.leftNode != None: nodeStack.append(node.leftNode)
                if node.rightNode != None: nodeStack.append(node.rightNode)

            return True

    # method to lock a node
    def lock(self):
        if self.isLocked == True: return True
        else: # not locked
            if self.areAncestorsUnlocked() or self.areDecendantsUnlocked():
                self.isLocked = True
                return True
            else:
                return False

    # method to unlock a node
    def unlock(self):
        if self.isLocked == False: return True
        else: # not locked
            if self.areAncestorsUnlocked() or self.areAncestorsUnlocked():
                self.isLocked = False
                return True
            else:
                return False


# function to print information about node (Only for testing purpose)
def printNode(node):
    print("============================================")
    print("Value : ", node.nodeValue)
    if node.leftNode != None:
        print("Left Node : ", node.leftNode.nodeValue)
    if node.rightNode != None:
        print("Right Node : ", node.rightNode.nodeValue)
    if node.parentNode != None:
        print("Parent Node : ", node.parentNode.nodeValue)
    print("Is Locked : ", node.isLocked)
    print("============================================\n")


if __name__ == "__main__":
    """
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \    /
         4   7  13
    """
    # Constructing a above drawn Tree of Nodes
    treeRoot = Node(nodeValue=8)
    treeRoot.leftNode = Node(3, parentNode=treeRoot)
    treeRoot.rightNode = Node(10, parentNode=treeRoot)
    treeRoot.leftNode.leftNode = Node(1, parentNode=treeRoot.leftNode)
    treeRoot.leftNode.rightNode = Node(6, parentNode=treeRoot.leftNode)
    treeRoot.rightNode.rightNode = Node(14, parentNode=treeRoot.rightNode)
    treeRoot.leftNode.rightNode.leftNode = Node(4, parentNode=treeRoot.leftNode.rightNode)
    treeRoot.leftNode.rightNode.rightNode = Node(7, parentNode=treeRoot.leftNode.rightNode)
    treeRoot.rightNode.rightNode.leftNode = Node(13, parentNode=treeRoot.rightNode.rightNode)

    # taking 6 (For testing purpose)
    testNode6 = treeRoot.leftNode.rightNode

    # before locking
    printNode(testNode6)

    # after locking
    testNode6.lock()
    printNode(testNode6)

    # taking 3 after locking 6 (For testing purpose)
    testNode3 = treeRoot.leftNode

    # before locking
    printNode(testNode3)

    # after locking
    testNode3.lock()
    printNode(testNode3)
