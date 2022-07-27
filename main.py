import time

def do_twice(func, arg):
    func(arg)
    func(arg)
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)
def right_justify(str):
    print((70 - len(str)) * ' ' + str)
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
def factorial(n: int):
    # Returns n * factorial of n if n > 1 else its returns 1
    return n * factorial(n - 1) if n > 1 else 1
def timeConvert():
    actualTime = time.time()
    secondsMinute = 60
    secondsHour = 60*60
    secondsDay = 24*60*60
    secondsMonth = 30.417 * secondsDay
    secondsYear = 12 * secondsMonth
    year = 1970 + (actualTime/secondsYear)
    month = 12 * (year-int(year))
    day = 1 + (actualTime/secondsDay)
    print(int(year))
    print(int(month))
    print(day)
def fermatTheorem(a, b, c, n):
    if n >= 2  and (a**n) + (b**2) == (c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")
def recurse(n, s):
    '''
    This function only works for positive numbers.
    It prints the sum of n and s every time it recurse it calls s with diferent number
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
if __name__ == '__main__':
    '''
    do_twice(print, 'spam')
    print('-' * 20)
    do_four(print, 'spam')
    print('-' * 20)
    right_justify('96000000')
    print(factorial(5))
    fermatTheorem(3, 4, 5, 2)
    timeConvert()
    recurse(5, 2)
    '''


'''
Old Format Method
Some Ways to Format Strings
name = input('What is your name? ')
print('Hi, %s.' % name)
'''