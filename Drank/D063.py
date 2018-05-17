import bisect
nums = list(map(int,input().split()))
a = int(input())
print(bisect.bisect_left(a))
#二分探索。ソート済み配列が渡されるのでアルゴリズム的にも一番早い
