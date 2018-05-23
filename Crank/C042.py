n = int(input())
wl = [list(map(int,input().split())) for x in range(n*(n-1)//2)]
results = [['-' for x in range(n)] for y in range(n)]
for a in wl:
  results[a[0]-1][a[1]-1] = 'W'
  results[a[1]-1][a[0]-1] = 'L'
for result in results:
  print(' '.join(result))
#入力はM行（M=n*(n-1)//2 )なので注意
