arr = [-3, 4, -1, 1]
minPosNum = 1

for elem in arr:

    # Accepting only positive integers
    if elem == 1:
        minPosNum = 2
    elif elem > 0:
        if elem < minPosNum:
            minPosNum = elem

print(minPosNum)