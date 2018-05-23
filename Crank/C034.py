a,b,c,d,e = input().split()
if b == '+':
  if e == 'x':
    print(int(a)+int(c))
  elif a == 'x':
    print(int(e)-int(c))
  else:
    print(int(e)-int(a))
else:
  if e == 'x':
    print(int(a)-int(c))
  elif a == 'x':
    print(int(c)+int(e))
  else:
    print(int(a)-int(e))
