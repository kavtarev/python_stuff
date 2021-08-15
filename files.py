from os import error


try:
    data = open('bs.txt', 'r')
    for line in data.readlines():
        print(line.strip())
        
except FileNotFoundError:
  print('non')
data.close()
#print('hi my name is',data.readable())
