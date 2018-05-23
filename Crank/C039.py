nums = input().split('+')
total = 0
for num in nums:
  if '<' in num:
    total += 10 * num.count('<')
  if '/' in num:
    total += num.count('/')
print(total)
