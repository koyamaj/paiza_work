a,b,R=map(int,input().split())
n = int(input())
trees = [list(map(int,input().split())) for x in range(n)]
for tree in trees:
  dist = pow(a-tree[0],2)+pow(b-tree[1],2)
  if pow(R,2) <= dist:
    print('silent')
  else:
    print('noisy')
