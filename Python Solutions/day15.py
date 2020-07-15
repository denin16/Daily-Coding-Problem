"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.
"""

import random

def spitElem():
    with open('stream.txt','r') as file:
        for num in file:
            yield num

if __name__ == "__main__":
    elemsToWrite = 1000000

    with open('stream.txt','w+') as file:
        for i in range(elemsToWrite):
            file.write(str(random.uniform(-100,100)) + "\n")

    for elem in spitElem():
        print(elem)


# Official Solution
"""
import random
def pickRandom(stream):
    random_element = None
    for i, e in enumerate(stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
"""
