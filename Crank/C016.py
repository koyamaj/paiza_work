dict = {'A':'4','E':'3','G':'6','I':'1','O':'0','S':'5','Z':'2'}
s = input().rstrip()
result = []
for i in range(len(s)):
  if s[i] in dict:
    result.append(dict[s[i]])
  else:
    result.append(s[i])
print(''.join(result))
