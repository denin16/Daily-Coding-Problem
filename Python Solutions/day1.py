"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Simple Solution O(n^2)

arr = [10, 15, 3, 7]
k = 17

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k:
            print(i, j)

     


# Solving it in one Pass O(n)

# Solution :

"""
1. Find the half of the given number i.e k
2. Make two sets from the given array arr, 
    containing (k - arr[i]) if number is less than or equal to the half,
    else put it as it is in second set
3. Find the intersection of the two sets (Gives you one part of each pair)
4. Subtract the values to find the second part of each pair.
"""
n = 181
n2 = n//2 # 90
numbers = [80, 98, 83, 92, 1, 38, 37, 54, 58, 89]
goodnums = {n-x for x in numbers if x<=n2} & {x for x in numbers if x>n2}
pairs = {(n-x, x) for x in goodnums}
print(pairs)