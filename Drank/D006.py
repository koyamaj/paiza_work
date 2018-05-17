n,s=input().split()
if s == 'km':
  print(1000*100*10*int(n))
elif s == 'm':
  print(100*10*int(n))
else:
  print(10*int(n))

#愚直すぎ（cm変換が冗長）なので以下の方が良い
"""
n,s=input().split()
dist_cm = int(n)*10
if s == 'cm':
  print(dist_cm)
elif s == 'm':
  print(100*dist_cm)
else:
  print(1000*100*dist_cm)
"""
