loto = list(map(int,input().split()))
n = int(input())
nums = [list(map(int,input().split()) for x in range(n)]
for num in nums:
  count = 0
  for i in range(6):
    if num[i] in loto:
      count += 1
  print(count)
