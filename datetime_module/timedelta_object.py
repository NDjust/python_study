'''
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

methods -  'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds'

'''

import datetime
td1 = datetime.timedelta(days=1)
# >> td1 = datetime.timedelta(1)

td2 = datetime.timedelta(days=-3)
# >> td2 = datetime.timedelta(-3)

td3 = td1 + td2
# >> td3 = datetime.timedelta(-2)

td4 = td1 -td2
# >> td3 = datetime.timedelta(4)

td5 = td1 * 3 -td2
# >> td5 = datetime.timedelta(6)

td6 = datetime.timedelta(days=5) / 2
# >> td6 = datetime.timedelta(2, 43200)

d = datetime.date(2017, 1, 1)
d + td1
# >> datetime.date(2017, 1, 2)


t = datetime.time(5)
# print(t + td1) -> Error 날짜가 정해지지 않은 시점(같은 시점)에서는 시간을 더하고 뺄 수 없다.
# t + datetime.timedelta(hours=2) -> Error

d2 = d + td1
# >> d2 = datetime.date(2017, 1, 2)

d2 = d + td1
print(d2)
print(d)

print(td2 < td1) # True



