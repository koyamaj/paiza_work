X,Y,P=map(int,input().split())
if X%Y == 0:
  print((X//Y)*P)
else:
  print((X//Y + 1)*P)
