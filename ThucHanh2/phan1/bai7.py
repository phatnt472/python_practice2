def same_first_last(L):
    '''Precondition: len(L) >= 2 
    Return True if and only if first item of list is the same as the last.
    >>> same_first_last([3,4,2,8,3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0,4.5])
    False
    '''
    return L[0] == L[len(L)-1] 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(same_first_last([3,4,2,8,3]))
    print(same_first_last(['apple', 'banana', 'pear']))
    print(same_first_last([4.0,4.5]))