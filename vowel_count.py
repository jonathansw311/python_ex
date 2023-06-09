def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels ='aeiou'
    map={}
    phrase = phrase.lower()
    for p in phrase:
        if p in vowels:
            if p in map.keys():
                map[p]= map[p] +1
            else:
                map[p]= 1

    return map            