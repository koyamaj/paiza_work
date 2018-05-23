n = int(input())
goods = [list(map(int,input().split())) for x in range(n)]
total = [0,0,0,0]
p = 0
for good in goods:
  total[good[0]] += good[1]
p = 5*(total[0]//100) + 3*(total[1]//100) + 2*(total[2]//100) + (total[3]//100)
print(p)
