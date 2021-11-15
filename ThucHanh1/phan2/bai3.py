def avarage(num1,num2):
    '''Return the average of num1 and num2.
    >>> avarage(10,20)
    15.0
    >>> avarage(2.5,3.0)
    2.75
    '''

    return (num1 + num2)/2
   



if __name__  ==  '__main__':
    import doctest
    doctest.testmod()