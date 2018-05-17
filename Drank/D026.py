days = [input() for i in range(7)]
count = 0
for day in days:
  if day == 'no':
    count += 1
print(count)

#条件反射で入力値を保持したが、noの入力だけ配列に入れてlenで答えを出しても良さそう
