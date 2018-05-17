a,b,c=map(int,input().split())
f = c/(a*b)
g,h,i=map(int,input().split())
s = i/(g*h)
if f == s:
  print('DRAW')
elif f < s:
  print(a,b,c)
else:
  print(g,h,i)
