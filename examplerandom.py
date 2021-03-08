import random
# If I name the file random, we cannot call random, because it will call itself.
for val in range(0,10):
    print(random.randint(1,10))

print("sum of 10 numbers")
sum = 0
for val in range (10):
    sum=sum+int(random.randint(0,10))
print(sum)

