a = input().rstrip()
b = input().rstrip()
if a[-1] == b[0] and b[-1] != 'n':
  print('OK')
else:
  print('NG')
