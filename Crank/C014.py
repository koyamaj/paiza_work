n,r=map(int,input().split())
boxs = [list(map(int,input().split())) for x in range(n)]
for i in range(n):
  if 2*r <= min(boxs[i]):
    print(i+1)
