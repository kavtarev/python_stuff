import random

num = 0
secret = random.randint(1,10)

while num != secret:
    num = int(input('enter number: '))
    if num > secret:
      print('number too high')
    elif num < secret:
      print('num is too low')
    else:
      print(f'correct number was {num}')
