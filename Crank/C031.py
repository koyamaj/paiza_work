n = int(input())
towns = [input().split() for x in range(n)]
times = {}

for town in towns:
  times[town[0]] = int(town[1])
q,t=map(str,input().split())
judge = times[q]

for i in range(n):
  hh = int(t[:2])+int(towns[i][1])-judge
  if hh < 0:
    hh += 24
  elif 24 <= hh:
    hh %= 24
  strhh = str(hh)
  if len(strhh) < 2:
    strhh = '0' + strhh
  print(strhh+t[2:])
