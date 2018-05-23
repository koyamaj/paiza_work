n = int(input())
comps = [input().split() for x in range(n)]
l,r=0,1000
for comp in comps:
  if comp[0] == 'ge':
    l = max(l,float(comp[1]))
  else:
    r = min(r,float(comp[1]))
print(l,r)
