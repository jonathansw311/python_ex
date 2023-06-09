m1 = [
             [1,   2],
             [30, 40],
         ]

m2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    idx = 0
    sum=0

    for list in matrix:
        sum= sum+ list[idx]
        if not (idx == len(matrix)-1): 
            idx = idx +1
        

    for list in matrix:
        sum = sum + list[idx]
        idx = idx -1
    
    return sum