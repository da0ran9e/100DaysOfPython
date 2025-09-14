#the rabbit problems: fibonacci number
#scenario--> 2 newborn rabbit: 1 male + 1 female
def fib(m):
 if m == 0 or m == 1:
  return 1
 else:
  return fib(m-1) + fib(m-2)
print(fib(12)) # T = 0(2^n)
#key concept
#     fibonacci sequence
#     reproduction  rate
#     population growth