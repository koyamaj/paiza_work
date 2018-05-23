a,b=map(str,input().split())
s = input().split(a)
tmp = ''
for i in range(1,len(s)):
  if b not in s[i]:
    tmp += s[i] + a
  else:
    tmp += (s[i].split(b))[0]
    if len(tmp) == 0:
      print('<blank>')
    else:
      print(tmp)
    tmp = ''
