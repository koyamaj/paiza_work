n = int(input())
tests = [input().split() for x in range(n)]
count = 0
for test in tests:
  if test[0] == 's':
    if 160 <= int(test[2])+int(test[3]) and 350 <= sum(list(map(int,test[1:]))):
      count += 1
  else:
    if 160 <= int(test[4])+int(test[5]) and 350 <= sum(list(map(int,test[1:]))):
      count += 1
print(count)
