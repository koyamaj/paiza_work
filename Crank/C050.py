s,a,b=map(int,input().split())

while 1:
  if s+10 <= a:
    s += 10
  else:
    print('B',s)
    break
  if s+1000 <=b:
    s += 1000
  else:
    print('A',s)
    break
