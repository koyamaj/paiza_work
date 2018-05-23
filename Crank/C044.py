n = int(input())
hands = ['paper','rock','scissors']
counts = [0]*3
for x in range(n):
  counts[hands.index(input().rstrip())] += 1
if 0 not in counts:
  print('draw')
elif counts.count(0) == 2:
  print('draw')
else:
  if counts[0] == 0:
    print(hands[1])
  elif counts[1] == 0:
    print(hands[2])
  else:
    print(hands[0])
