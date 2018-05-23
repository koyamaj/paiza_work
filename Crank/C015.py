n = int(input())
recs = [list(map(int,input().split())) for x in range(n)]
point = 0
for r in recs:
  if '3' in str(r[0]):
    point += (r[1]*3)//100
  elif '5' in str(r[0]):
    point += (r[1]*5)//100
  else:
    point += r[1]//100
print(point)
