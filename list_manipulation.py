def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end')
        True

        >>> list_manipulation(lst, 'add', 'dunno') 
        True
    """
    if command is not 'add' and command is not 'remove':
        return True
    if location is not 'beginning' and location is not 'end':
        return True
    
    if command == 'remove':
        if location == 'end':
            return lst.pop()
        if location == 'beginning':
            return lst.pop(0)

    if command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        if location == 'end':
            lst.append(value)
            return lst