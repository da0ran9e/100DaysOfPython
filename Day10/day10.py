#sequence sum
# formula: 1/1! + 2/2!....

n= int(input('enter n:'))
result = 0
fact = 1
for i in range(1, n+1):
 fact *= i
 result += i/ fact
print(result)
