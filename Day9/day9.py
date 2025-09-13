import random
jackpot = random.randint(1,100)
guess  = int(input('chal guess kar:'))
counter = 1
while guess != jackpot:
 if guess < jackpot:
  print('guess higher')
 elif guess > jackpot:
  print('guess lower')
 guess = int(input('chal guess kar:'))
 counter +=1
print('sahi Jawab')
print (' you took', counter, ' attempt')