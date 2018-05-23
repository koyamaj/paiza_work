m,n=map(int,input().split())
rains = [list(map(int,input().split())) for x in range(m)]
result = 100
minp = pow(10,8)
for i in range(m-n+1):
  prop = 0
  for j in range(n):
    prop += rains[i+j][1]
  if prop < minp:
    minp = prop
    result = rains[i][0]
print(result,result+n-1)
