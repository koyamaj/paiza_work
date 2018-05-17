days = [int(input()) for i in range(7)]
count = 0
for day in days:
  if day <= 30:
    count += 1
print(count)
