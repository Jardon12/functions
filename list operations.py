import random
a = [1, 2, 3]
a.append(7)
print(a)
a.remove(3)
#I remove the value
print(a)
a.pop(1)
# I remove the position
print(a)

a =[]
for element in range (0, 10):
    a.append(random.randint(1,100))
print(a)

del a[::2]
print(a)

while a:
    print(a.pop(0))






