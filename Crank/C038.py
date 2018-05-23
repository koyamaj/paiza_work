m,n=map(int,input().split())
macs = [int(input()) for x in range(m)]
cas = 0
mod = 10000
res = 999
for i in range(m):
  if mod == (n%macs[i]):
    if cas < macs[i]:
      cas = macs[i]
      res = (i+1)
  elif (n%macs[i]) < mod:
    cas = macs[i]
    mod = n%macs[i]
    res = (i+1)
print(res)
