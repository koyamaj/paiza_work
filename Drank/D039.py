nodes = [int(input()) for i in range(3)]
if max(nodes) == min(nodes):
  print('YES')
else:
  print('NO')

# 3辺比較（aとb,bとc,cとa）より、最大＝最小を見た方が早い
