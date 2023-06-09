def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    count = 0
    leng = len(nums)
    advance =1
    idx = 1
    
    for num in nums:
        print(f"number is {num}")
        while idx < len(nums):   
            if num < nums[idx]:
                count += 1
                idx +=1
            else:
                idx += 1
        nums.pop(0)
        idx = 1
        print(nums)
    return count

