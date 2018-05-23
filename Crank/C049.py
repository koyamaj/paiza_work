n = int(input())
nums = [int(input()) for x in range(n)]
total = 0
for i in range(1,n):
  total += abs(nums[i] - nums[i-1])
print(total+nums[0]-1)
