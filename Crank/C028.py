n = int(input())
tests = [input().split() for x in range(n)]
count = 0
for test in tests:
  if len(test[0]) == len(test[1]):
    miss = 0
    for i in range(len(test[0])):
      if (test[0])[i] != (test[1])[i]:
        miss += 1
    if miss < 1:
      count += 2
    elif miss < 2:
      count += 1
print(count)
