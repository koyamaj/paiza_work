import math
m=int(input())
n=int(input())
faxs = [list(map(int,input().split())) for x in range(n)]
hh,paper,count = 0,0,0
for fax in faxs:
  if hh < fax[0]:
    count += math.ceil(paper/m)
    hh = fax[0]
    paper = fax[2]
  else:
    paper += fax[2]
count += math.ceil(paper/m)
print(count)
