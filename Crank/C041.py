n = int(input())
country = [list(map(int,input().split())) for x in range(n)]
country.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)
for c in country:
  print(c[0],c[1],c[2])
