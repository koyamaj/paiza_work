n = int(input())
names = input().split()
m = int(input())
books = [input().split() for x in range(m)]
result = []
for name in names:
  total = 0
  for book in books:
    if name in book:
      total += int(book[1])
  result.append(name,total)
result.sort(key=lambda x:x[1],reverse=True)
for r in result:
  print(r[0])
