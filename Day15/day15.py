def is_even(num):
 '''
 this function tells if a given num is odd or even
 input - any valid integer
 output - odd/even
 '''
 if type(num) == int:
  if num % 2 == 0:
   return'even'
  else:
   return'odd'
 else:
  return' not allowed'
for i in range(1, 11):
 print(is_even(i))
print(is_even.__doc__)