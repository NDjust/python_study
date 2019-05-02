class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


if __name__ == "__main__":
    hong = Person('nathan')
    hong_email = EmailPerson('na', "skeks463@gmail.com")
    print(hong.name)
    print(hong_email.name)
    print(hong.name)