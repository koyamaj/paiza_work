n = input().rstrip()
m = int(input())
rooms = [input().rstrip() for x in range(m)]
count = 0
for room in rooms:
  if n not in room:
    print(room)
    count += 1
if count == 0:
  print('none')
