def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    nphrase = list(phrase)
    nphrase.reverse()
    revphrase = ''.join(nphrase)
    return revphrase
