m,n = map(int,input().split())
arrays = [str(m+n*i) for i in range(10)]
print(' '.join(arrays))
