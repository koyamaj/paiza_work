H,W=map(int,input().split())
picts = [list(map(int,input().split())) for x in range(H)]
for i in range(H):
  tmp = list()
  for j in range(W):
    if picts[i][j] <=127:
      tmp.append('0')
    else:
      tmp.append('1')
  print(' '.join(tmp))
