points = list(map(int,input().split()))
x = int(input())
if x <= sum(points)//len(points):
  print('pass')
else:
  print('failure')
