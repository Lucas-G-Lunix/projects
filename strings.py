'''
def rotate_word(word, n):
    """
    Rotates a word by n characters
    """
    word_codes = []
    for letter in word:
        word_codes.append(ord(letter))
    rotated_word = []
    for code in word_codes:
        rotated_word.append(chr(code + n))
    return "".join(rotated_word)
'''

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res
if __name__ == '__main__':
    print(rotate_word("melon", -10))
