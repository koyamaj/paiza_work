day,times = input().split()
if int(times[:2]) < 24:
  print(day,times)
else:
  hh = int(times[:2])
  adday = hh//24
  hh = hh%24
  sthh = str(hh)
  stday = str(int(day[3:])+adday)
  if len(stday) < 2:
    stday = '0'+stday
  if hh < 10:
    sthh = '0'+str(hh)
  print(day[:3]+stday,sthh+times[2:])
#日付・時刻ともに1桁になる可能性があるので'0'埋めが必要
