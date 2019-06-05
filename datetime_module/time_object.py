import datetime


t = datetime.time(5) # datetime.time(hour, minute, second, micro second)


t1 = datetime.time(6, 23, 0, 100)
t2 = datetime.time(6, 23, 0, 100)
print(t1)
print(t1.isoformat())
print(str(t1))
print(t1.strftime("%H:%M:%S"))
print(t1 == t2)
print(t1 is t2)


# 출력값.
# 06:23:00.000100
# 06:23:00.000100
# 06:23:00.000100
# 06:23:00
# True
# False