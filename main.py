def do_twice(func, arg):
    func(arg)
    func(arg)
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)
def right_justify(str):
    print((70 - len(str)) * ' ' + str)

if __name__ == '__main__':
    do_twice(print, 'spam')
    print('-' * 20)
    do_four(print, 'spam')
    print('-' * 20)
    right_justify('96000000')




'''
Some Ways to Format Strings
name = input('What is your name? ')
print('Hi, %s.' % name)
'''