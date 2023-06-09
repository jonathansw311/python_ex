def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict = {}
    count_list=[]
    num_set = set(nums)
    
    for num in num_set:
       count= nums.count(num)
     # count_list.append(count)
    
    count = 0
    for num in num_set:
       
        dict[num]=count_list[count]
        count = count + 1
        

    maxs = max(dict.values())

    maxxs = [v for v in dict if dict[v]== maxs]
    return maxxs