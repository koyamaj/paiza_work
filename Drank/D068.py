n = int(input())
s = input().rstrip()
if 'S' in s:
  print(s.count('S'),n-s.count('S'))
else:
  print(0,n)
