def total_occurences(s1,s2,ch):
    """(str,str,str) -> (str,str,str)
    Precondition: len(ch) == 1 
    Return the total number of times that ch occurs in s1 and s2
    >>> total_occurences("color","yellow","l")
    3
    >>> total_occurences("red","blue","l")
    1
    >>> total_occurences("green","purple","b")
    0
    """
    return s1.count(ch)+s2.count(ch)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(total_occurences("color","yellow","l"))
print(total_occurences("red","blue","l"))
print(total_occurences("green","purple","b"))