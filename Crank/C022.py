n = int(input())
prices = [list(map(int,input().split())) for x in range(n)]
highest,lowest = 0,9000000
for price in prices:
  highest = max(highest,price[2])
  lowest = min(lowest,price[3])
print((prices[0])[0],(prices[-1])[1],highest,lowest)
