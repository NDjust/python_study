import datetime

today = datetime.date.today() # datetime에 date 객체 today() 멤버 함수 접근.

print(today) # datetime.date(year, month,day)


date1 = datetime.date(2016, 5, 2)
# date 객체에 직접 멤버 변수 할당해서 생성.

date2 = datetime.date(2016, 5, 2)

print(date1 == date2) # True
print(date1 is date2) # False -> 서로 다른 메모리 사용.

# date3 = datetime.date(2015, 12 ,40) -> error

print(date1.isoformat()) # 2016-05-02
print(str(date1)) # 2016-5-2
print(date1.ctime()) # "요일 월 00:00:00 2016"
print(date1.strftime("%y/%m/%d")) # 16/05/02
print(date1.year) # 2016 -> datetime에 date 객체는 year, month, day를 decorator property를 사용해 접근.
print(date1.year)
print(date1.weekday()) # monday(0) ~ sunday(6)
print(date1.isoweekday()) # monday(1) ~ sunday(7)
