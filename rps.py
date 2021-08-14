import random

def game():
  you = input('input s for scissors r for rock p for paper\n')
  print(f'hi ---- {you}')
  cpu = random.choice(['s','p','r'])

  if is_Won(you,cpu):
    return('you won')
  if you == cpu :
    return('tie')
  return('you lose')

def is_Won(one,two):
  if (one=='s' and two == 'p') or (one == 'p' and two == 'r') or (one == 'r' and two == 's'):
    return True
print(game())