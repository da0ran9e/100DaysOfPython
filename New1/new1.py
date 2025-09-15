a = int(input('enter the first age:'))
b = int(input('enter the second age:'))
c = int(input('enter the third age:'))
max_age = a
if max_age < b:
    max_age = b
if max_age < c:
    max_age = c
print(max_age)