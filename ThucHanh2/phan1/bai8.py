def is_longer(L1,L2):
    '''Return True if and only if the length of L1 is longer than the length of L2
    >>> is_longer([1,2,3],[4,5])
    True
    >>> is_longer(['abcdef'],['ab','cd','ef'])
    False
    >>> is_longer(['a','b','c'],[1,2,3])
    False
    '''
    return len(L1) > len(L2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('',is_longer([1,2,3],[4,5]),'\n',is_longer(['abcdef'],['ab','cd','ef']),'\n',is_longer(['a','b','c'],[1,2,3]))