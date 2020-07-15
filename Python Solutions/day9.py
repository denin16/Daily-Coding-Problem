"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def maxNonAdjSum(arr):
    arrLen = len(arr)
    dpArr = [None] * arrLen
    dpArr[0] = arr[0]
    dpArr[1] = max(arr[0], arr[1])
    
    for i in range(2, arrLen):
        dpArr[i] = max(dpArr[i-1], dpArr[i-2] + arr[i])

    return dpArr[-1]

if __name__ == "__main__":
    testArr1 = [2, 4, 6, 2, 5]
    testArr2 = [5, 1, 1, 5]

    print("Max sum of : ", testArr1, " is -> ", maxNonAdjSum(testArr1))
    print("Max sum of : ", testArr2, " is -> ", maxNonAdjSum(testArr2))
