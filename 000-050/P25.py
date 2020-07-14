def fibonacci(digits):
    """ 
    Generates a fibonacci sequence and stops upon getting the first term with 'n' digits
    Returns the term's position. 
    """
    if digits == 1:
        return 1
    val1 = 1
    val2 = 1
    index = 2
    while True:
        index +=1
        val1 = val1 + val2
        if len(str(val1)) == digits:
            return index
        index +=1
        val2 = val2 + val1
        if len(str(val2)) == digits:
            return index
    
print(fibonacci(1000))