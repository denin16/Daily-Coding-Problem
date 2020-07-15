"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time

def jobScheduler(job, interval):
    milliInterval = interval / 1000
    time.sleep(milliInterval)
    job()

def firstFunc():
    print("First Function")

def secondFunc():
    print("Second Function")

def thirdFunc():
    print("Third Function")    

if __name__  == "__main__":
    jobScheduler(firstFunc, 2000)
    jobScheduler(secondFunc, 3000)
    jobScheduler(thirdFunc, 150)
