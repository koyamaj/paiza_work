n = int(input())
nums = list(map(int,input().split()))
sums = [0]*(max(nums)+1)
for num in nums:
  sums[num] += 1
result = list()
for i in range(len(sums)):
  if sums[i] == max(sums):
    result.append(str(i))
print(' '.join(result))
