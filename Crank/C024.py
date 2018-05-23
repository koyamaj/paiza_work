n = int(input())
Slist = [input().split() for x in range(n)]
vals = [0,0]
for s in Slist:
  if s[0] == 'SET':
    vals[int(s[1])-1] = int(s[2])
  elif s[0] == 'ADD':
    vals[1] = vals[0] + int(s[1])
  else:
    vals[1] = vals[0] - int(s[1])
print(vals[0],vals[1])
