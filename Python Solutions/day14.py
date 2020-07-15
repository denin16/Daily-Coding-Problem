"""
Question 14 (Medium)

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

import random

INTERVAL = 1000

circlePoints = 0
squarePoints = 0

for i in range(INTERVAL**2):
    randX = random.uniform(-1,1)
    randY = random.uniform(-1,1)

    d = randX**2 + randY**2

    if d <= 1:
        circlePoints += 1

    squarePoints += 1
    pi = 4 * circlePoints/squarePoints

print("Estimated Pi : ", pi)
