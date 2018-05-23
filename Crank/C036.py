a,b = map(int,input().split())
c,d = map(int,input().split())
times1 = list(map(int,input().split()))
times2 = list(map(int,input().split()))
cand1,cand2 = 10,10
if times1[a-1] < times1[b-1]:
  cand1 = a
else:
  cand1 = b
if times1[c-1] < times1[d-1]:
  cand2 = c
else:
  cand2 = d
if times2[0] < times2[1]:
  print(min(cand1,cand2))
  print(max(cand1,cand2))
else:
  print(max(cand1,cand2))
  print(min(cand1,cand2))
