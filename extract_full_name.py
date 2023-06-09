names = [
            {'first': 'Ada', 'last': 'Lovelace'},
            {'first': 'Grace', 'last': 'Hopper'},
        ]


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    name_list = []
    for name in names:

      f_names = str(name['first'])
      l_names = str(name['last'])
      name = f'{f_names} {l_names}'
      name_list.append(name)
    
    return name_list
      

