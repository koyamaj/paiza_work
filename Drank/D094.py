cat,dog = 0,0
for i in range(3):
  if input().rstrip() == 'cat':
    cat += 1
  else:
    dog += 1
if cat < dog:
  print('dog')
else:
  print('cat')
