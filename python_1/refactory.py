small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')


def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    lst_of_words = title.lower().split()

    if len(lst_of_words) < 1:
        return ''

    new_title = lst_of_words.pop(0).title()

    title = new_title + ' ' + ' '.join(
        [word if word in small_words else word.title()
         for word in lst_of_words])

    return title


def _test():
    import doctest
    import refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
