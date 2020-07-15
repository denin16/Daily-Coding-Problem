"""
Question 18 (Hard)
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of 
each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.

"""
import math

def subArraysMax(arr, k):
    arrLen = len(arr)
    arrMax = arr[0]
    tempArrMax = arr[1]
    arrEnd = 1
    
    for i in range(1, arrLen):
        if arrMax < arr[i]:
            arrMax = arr[i]
        
        if tempArrMax < arr[i] and arrMax > arr[i]:
            tempArrMax = arr[i]

        if i == arrEnd:
            print(arrMax)
            arrMax = tempArrMax
            arrEnd += 1



if __name__ == "__main__":
    array = [10, 5, 2, 7, 8, 7]
    k = 3

    subArraysMax(array, k)