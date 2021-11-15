def remove_neg(num_list: list):
    """Remove the nagative numbers from the list num_list
    >>> numbers = [1,-5,-3,2]  
    >>> remove_neg(numbers)
    [1, 2]
    """
    i = 0
    while i < len(num_list):
        if num_list[i] <  0:
            del num_list[i]
        else:
            i+=1
    return num_list
 

if __name__ == '__main__':
    import doctest 
    doctest.testmod()
