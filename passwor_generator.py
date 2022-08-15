import random
lettersMayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lettersMinus = lettersMayus.lower()
numbers = '1234567890'
symbols = '!@#$%^&*'
all = lettersMayus + lettersMinus + numbers + symbols

password = ''.join(random.sample(all, 10))
print(password)
