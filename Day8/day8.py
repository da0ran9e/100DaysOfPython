#average of num until 0
count = 0
total = 0
while True:
 num = int(input('enter a num ( 0 to stop ):'))
 if num == 0:
  break
 total += num
 count += 1
if count > 0:
 average = total / count
 print(f' average of entered nums:{average}')
else:
 print(' no nums entered')
