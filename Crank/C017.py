a,b=map(int,input().split())
n=int(input())
cards = [list(map(int,input().split())) for x in range(n)]
for card in cards:
  if a == card[0]:
    if b < card[1]:
      print('High')
    else:
      print('Low')
  elif a < card[0]:
    print('Low')
  else:
    print('High')
