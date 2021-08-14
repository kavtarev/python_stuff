import random

def pick(x):
    low = 1
    high = x
    
    user_input = ''

    if high == low:
      print('corrupted')
    else:
      while user_input != 'c':
        guess = random.randint(low, high)
        print(f'computer guess is {guess}')
        user_input = input('enter (h) for high (l) for low (c) for correct: ')
        if user_input == 'h':
            high = guess - 1
        if user_input == 'l':
            low = guess + 1
        else:
          print('coreecto')

pick(10)
