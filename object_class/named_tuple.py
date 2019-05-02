from collections import namedtuple

User = namedtuple("User", "name age") # namedtuple(이름, 스페이스로 구분된 필드 이름의 문자열)
user1 = User("nathan", 23)
print(user1)
print(user1.name)
print(user1.age)

user2 = user1._replace(age=24, name="dan")
print(user2)

parts = {"name": "hong", "age": 24}
user3 = User(**parts) # 키워드 인자 parts의 키와 값을 추출하여 User의 인자로 제공.
print(parts)