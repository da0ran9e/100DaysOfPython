#x = lambda x : x**2
#print(x(9))



#a = lambda x, y : x+y
#print(a(4,5))


L = [11, 14, 27, 21, 23, 56, 78, 39, 45, 29, 28, 30]
def return_sum(func, L):
 result = 0
 for i in L:
  if func(i):
   result = result + i
 return result
x = lambda x : x%2 == 0 # even sum
y = lambda x : x%2 != 0 # odd sum
z = lambda x : x%3 == 0 # div3 sum
print(return_sum(x, L))
print(return_sum(y, L))
print(return_sum(z, L))