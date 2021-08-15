arr = [1,2,4]
arr2 = arr.copy()
arr.pop()
a= [item if item in arr2 else 'kiki' for item in arr]
name = 'guga'

print(arr2)