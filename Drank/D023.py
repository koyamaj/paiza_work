s = input().rstrip()
if 'A' not in s:
  print('0')
else:
  print(s.count('A'))

# countは見つからないとErrorを返す仕様なので注意（return 0 は起こり得ない）
