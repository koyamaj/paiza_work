days = list(map(int,input().split()))
count = 0
for day in days:
  if day <=2:
    count += 1
print(count)
