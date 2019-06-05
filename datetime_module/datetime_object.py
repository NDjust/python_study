import datetime

tod = datetime.datetime.today() # 
print(tod) # 2019-06-05 19:14:53.089353

# datetime.datetime(year, month, day, hour, minute, second, micro second)

d = datetime.date(2002, 2, 20)
t = datetime.time(11, 20)
d_t = datetime.datetime.combine(d, t)
print(d_t) # 2002-02-20 11:20:00
print(d_t.isocalendar()) # (2002, 8, 3)
print(d_t.timetuple())

'''
d= datetime.datetime(2010, 1, hour=20) 
>> Error
d = datetime.datetime(2010, 1, 1, minute=20)
>> d= datetime.datetime(2010, 1, 1, 0, 20)
d = datetime.datetime(2010, 1, 1)
>> d = datetime.datetime(2010, 1, 1, 0, 0)
d = datetime.datetime(2010)
>> Error
'''