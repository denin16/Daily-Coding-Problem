# function to find words while expands forward from a position
def expand(inputList, inputString):
    stringList = []
    strLen = len(inputString)
    endIndex = 0
    for i in range(strLen):
        if i < endIndex:
            continue

        for j in range(i+1, strLen+1):
            if (inputString[i:j]) in inputList:
                stringList.append(inputString[i:j])
                endIndex = j
                break
    return stringList

# function to find words while shrinking to a position
def shrink(inputList, inputString):
    stringList = []
    strLen = len(inputString)
    endIndex = 0
    for i in range(strLen):
        if i < endIndex:
            continue

        for j in range(strLen, -1, -1):
            if (inputString[i:j]) in inputList:
                stringList.append(inputString[i:j])
                endIndex = j
                break
        
    return stringList

def originalSentenceList(inputList, inputString):
    """
    steps:
    expanding pass -> construct words in an expanding way (if word present in list, then add it to result list)
    shrinking pass -> construct words in a shrinking way (if word present in list, then add it to result list)
    """
    expandingList = expand(inputList, inputString)
    print(expandingList)

    shrinkingList = shrink(inputList, inputString)
    print(shrinkingList)
    

if __name__ == "__main__":
    inputList1 = ['quick', 'brown', 'the', 'fox']
    inputString1 = "thequickbrownfox"

    inputList2 =  ['bed', 'bath', 'bedbath', 'and', 'beyond']
    inputString2 = "bedbathandbeyond"

    #originalSentenceList(inputList1, inputString1)
    originalSentenceList(inputList2, inputString2)

