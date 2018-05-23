x,p = map(int,input().split())
total = 0
while 0 < x:
  total += x
  x = x*(100-p)//100
print(total)
#うまく計算すればO(1)で答えが出そうだが、値が小さいので愚直に実装した方が早そう。
