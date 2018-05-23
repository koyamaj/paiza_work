x,y,r1,r2=map(int,input().split())
n = int(input())
people = [list(map(int,input().split())) for x in range(n)]
for p in people:
  dist = (x-p[0])*(x-p[0]) + (y-p[1])*(y-p[1])
  if r1*r1 <= dist and dist <= r2*r2:
    print('yes')
  else:
    print('no')
