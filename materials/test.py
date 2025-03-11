n = int(input('input the number'))
total = 0
for i in range(1, n+1):
    total = total + (n//i)
print(total)