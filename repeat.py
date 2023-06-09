def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1)
        True

        >>> repeat('abc', 'nope')
        True
    """
    isInt = isinstance(num, int)
    if isInt == False:
        return True
   
    if not num >= 0:
        return True
   

    return phrase * num