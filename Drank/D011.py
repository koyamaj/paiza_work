s =input().rstrip()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alpha.index(s)+1)

#問題文にalphaに設定した文字列が記載されているのでこの実装が早い（気がする）
#記載がない（英大文字が入力される制約のみ）なら以下の通り（Aから数えて何番目？
'''
s = input().rstrip()
print(ord(chr(s)) - ord('A') + 1)

'''
