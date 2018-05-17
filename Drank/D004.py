n = int(input())
strlist = [input().rstrip() for x in range(n)]
print('Hello ' + ','.join(strlist) + '.')
