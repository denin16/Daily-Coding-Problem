"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def lonestSubstring(string, k):
    strLen = len(string)
    longestSubstr = ""
    for i in range(strLen):
        substring = ""
        distinctChars = set() #Initializing an empty set
        for j in range(i, strLen):

            if string[j] in distinctChars: # character already in distinct characters
                substring += string[j]

            else: # character not in distinct character set
                tempDistinctChars = set(distinctChars)
                tempDistinctChars.add(string[j])
                if len(tempDistinctChars) > k:
                    break
                    
                substring += string[j]
                distinctChars.add(string[j])
            
            if len(substring) > len(longestSubstr):
                    longestSubstr = substring
            
    return longestSubstr

if __name__ == "__main__":
    s = "abcba"
    k = 2
    print(lonestSubstring(s,k))

