"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class Tree:

    class Node:
        def __init__(self, value):
            self.value = value
            self.pointerArr = [] # initializing an empty pointer array
            self.numOfPointers = len(self.pointerArr)

    def __init__(self, dictArr):
        self.root = self.Node("Root")
        for word in dictArr:
            self.addWord(word)

    # Method to add word to the tree
    def addWord(self, word):
        self.temp = self.root
        for char in word:
            self.addChar(char)

    # Method to add character to the tree
    def addChar(self, char):

        if len(self.temp.pointerArr) == 0: # Tree is not initialized / No subtree
            self.temp.pointerArr.insert(0, self.Node(char))
            self.temp = self.temp.pointerArr[0]

        else: # Tree is initialised / Need to add characters to it
            try:

                if len(self.temp.pointerArr) == 1: # if length of pointer array is one
                    if  char < self.temp.pointerArr[0].value:
                        self.temp.pointerArr.insert(0, self.Node(char))
                        self.temp = self.temp.pointerArr[0]
                    elif char > self.temp.pointerArr[0].value:
                        self.temp.pointerArr.insert(1, self.Node(char))
                        self.temp = self.temp.pointerArr[1]
                    else:
                        self.temp = self.temp.pointerArr[0]

                else: # if it contains pointers to many nodes
                    inserted = False 
                    index = 0
                    for node in self.temp.pointerArr:
                        if node.value == char:
                            self.temp = node
                            inserted = True
                            break
                        elif node.value > char:
                            print("Char {char} entered this loop".format(char=char))
                            insertIndex = index
                            self.temp.pointerArr.insert(insertIndex, self.Node(char))
                            self.temp = self.temp.pointerArr[insertIndex]
                            inserted = True
                            break
                        index += 1

                    if not inserted:
                        self.temp.pointerArr.append(self.Node(char))
                        self.temp = self.temp.pointerArr[-1]

            except IndexError:
                print("Error During adding : ", char)
    

    # Method to find strings with the given string as initial string
    def findStrings(self, initString=""):
        root = self.root
        tempRoot = root

        # Find till is matches with string
        for char in initString:
            for node in tempRoot.pointerArr:
                if char == node.value:
                    tempRoot = node
        
        """ 
        Applying Depth First Search (DFS) to find all the strings possible from a node
        """

        stack = []
        stack.append(tempRoot)
        strToReturn = initString
        strsToReturn = []
        startConcat = False

        while(len(stack) != 0):
            node = stack.pop(-1)
            if startConcat == False:
                startConcat = True
            else:
                strToReturn += node.value

            # Checking for leaf node
            if len(node.pointerArr) == 0:
                strsToReturn.append(strToReturn)
                strToReturn = initString

            for i in range(len(node.pointerArr)-1, -1, -1):
                    stack.append(node.pointerArr[i])
            
        return strsToReturn

            
if __name__ == "__main__":
    dictArr = ["deal", "deer", "dog", "depth", "dope", "dull"]
    dictTree = Tree(dictArr)
    strings = dictTree.findStrings("de")
    print(strings)

    