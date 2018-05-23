n = int(input())
recp = [input().split() for x in range(n)]
m = int(input())
food = [input().split() for y in range(m)]
fdict = {}
for f in food:
  fdict[f[0]] = int(f[1])
minr = pow(10,10)
for r in recp:
  if r[0] in fdict:
    minr = min(minr,fdict[r[0]]//int(r[1]))
  else:
    print(0)
    exit()
print(minr)
