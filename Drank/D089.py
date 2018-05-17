import re
s = input().rstrip()
match = re.findall(r'[0-9]',s)
print(''.join(match))

#問題の制約が甘いのでコレでいける。数値＋文字列で文字列に数字が含まれる場合、各数字間の距離をとって連続性を確認する必要がある。
