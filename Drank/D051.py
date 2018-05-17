clothes = input().split()
count = 0
for c in clothes:
  if c == 'W':
    count += 1
if 5 <= count:
  print('OK')
else:
  print('NG')
