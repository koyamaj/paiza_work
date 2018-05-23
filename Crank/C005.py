n = int(input())
ips = [input() for x in range(n)]
for ip in ips:
  if '.' not in ip:
    print('False')
    continue
  else:
    if ip.count('.') != 3:
      print('False')
      continue
    else:
      tmp = ip.split('.')
      if len(tmp) != 4:
        print('False')
        continue
      else:
        count = 0
        for i in range(4):
          if tmp[i] == '':
            print('False')
            break
          elif int(tmp[i]) < 0 or 255 < int(tmp[i]):
            print('False')
            break
          elif int(tmp[i]) < 10 and 1 < len(tmp[i]):
            print('False')
            break
          else:
            count += 1
        if count == 4:
          print('True')
