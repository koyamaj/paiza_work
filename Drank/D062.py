alpha = [chr(i) for i in range(ord('A'),ord('J')+1)]
a,b,c = map(int,input().split())
print(''.join(alpha[:a]))
print(''.join(alpha[a:a+b]))
print(''.join(alpha[a+b:]))
