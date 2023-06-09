def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    other_case = to_swap.swapcase()
    new_string = ""
    for letter in phrase:
        if letter == to_swap or letter == other_case:
            new_string= new_string + letter.swapcase()
        else:
            new_string= new_string + letter
    return new_string            