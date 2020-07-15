# Outer function
def cons(a, b):

    # Inner function
    def pair(f):
        return f(a,b)

    # Returns inner function as an object
    return pair

# Returns first value from pair
def firstVal(a, b):
    return a

# Return second value from pair
def secondVal(a, b):
    return b

# Takes the object of pair function and executes it for first value
def car(pairFuncObj):
    carVal = pairFuncObj(firstVal)
    return carVal
    
# Takes the object of pair function and executes it for second value
def cdr(pairFuncObj):
    cdrVal = pairFuncObj(secondVal)
    return cdrVal


if __name__ == "__main__":
    """
    pairFuncObj = cons(3,4)
    carVal = pairFuncObj(car)
    cdrVal = pairFuncObj(cdr)
    print(carVal, cdrVal)
    """

    carValue = car(cons(3, 4)) #3
    cdrValue = cdr(cons(3, 4)) #4

    print(carValue, cdrValue)


    