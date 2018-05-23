n = int(input())
ball,strike=0,0
for i in range(n):
  tmp = input().rstrip()
  if tmp =='ball':
    ball += 1
    if 4 <= ball:
      print('fourball!')
      break
    else:
      print('ball!')
  else:
    strike += 1
    if 3 <= strike:
      print('out!')
      break
    else:
      print('strike!')
