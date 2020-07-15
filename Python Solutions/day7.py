def findNumOfWays(arr):
    numOfWays = 0
    waysArr = [0 for i in range(len(arr)+1)]
    waysArr[0] = 1
    waysArr[1] = 1

    if len(arr) == 1:
        return 1
    
    else:
        for i in range(2, len(waysArr)):
            if arr[i-1] > 0:
                waysArr[i] += waysArr[i-1]
            twoDigitsNum = int(str(arr[i-2]) + str(arr[i-1]))
            if twoDigitsNum >= 10 and twoDigitsNum <= 26:
                waysArr[i] += waysArr[i-2]
        numOfWays = waysArr[-1]

    return numOfWays


if __name__ == "__main__":
    arr = [1,1,2,2]
    numOfWaysArr = findNumOfWays(arr)
    print(numOfWaysArr)
    
