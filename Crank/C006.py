n,m,k = map(int,input().split())
params = list(map(float,input().split()))
users = [list(map(int,input().split())) for x in range(m)]
results = []
for user in users:
  total = 0
  for i in range(n):
    total += params[i]*user[i]
  results.append(int(total*2+1)//2)
results.sort(reverse=True)
for j in range(k):
  print(results[j])
