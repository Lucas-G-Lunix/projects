def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
# r edivide r  ------ noon
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

def is_power(a, b):
    if a == b:
        return True
    if a % b != 0:
        return False
    return is_power(a/b, b)


print(is_power(16, 8))
