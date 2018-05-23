n,s,p=map(int,input().split())
carrots = [list(map(int,input().split())) for x in range(n)]
weight = 0
index = 1000
for i in range(n):
  if s-p <= carrots[i][1] and carrots[i][1] <= s+p and weight < carrots[i][0]:
    index = i+1
    weight = carrots[i][0]
if index == 1000:
  print('not found')
else:
  print(index)
