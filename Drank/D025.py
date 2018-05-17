n = input().rstrip()
if 3 <=len(n):
  print(n[:3])
else:
  result = '0'*(3-len(n)) + n
  print(result)

#地味にnの値域が広い(n<=100)ので注意する
