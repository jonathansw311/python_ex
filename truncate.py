def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    new_string = ""
    length = len(phrase)
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    
    if length < n-4:
        return phrase
    
    idx=0

    for letter in phrase:
        if not idx == n-3:
            new_string= new_string + letter
            idx = idx +1
        else:
            new_string = new_string + "..."
            return new_string
    
    

    

