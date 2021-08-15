from os import error


try:
    data = open('bs1.txt', 'a')
    data.write('new line2 \n')
    
        
except FileNotFoundError:
  print('non')
data.close()
#print('hi my name is',data.readable())
