def getS(x):
  result = 0
  for i in range(1,x):
    if x%i==0:
      result += i
  return result
Q = int(input())
for j in range(Q):
  tmp = int(input())
  S = getS(tmp)
  if tmp == S:
    print('perfect')
  elif abs(tmp-S) == 1:
    print('nearly')
  else:
    print('neither')
#制約上、ループ回数が少ない（高々5*10^5）ので全探索
