n,s,p=map(int,input().split())
result = []
if (p-1)*s+1 <= n:
  for i in range((p-1)*s+1,min(n+1,p*s+1)):
    result.append(str(i))
if 0 < len(result):
  print(' '.join(result))
else:
  print('none')
