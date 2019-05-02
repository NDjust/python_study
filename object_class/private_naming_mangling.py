class Duck:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, new_name):
        print("inside the setter")
        self.hidden_name = new_name


class Duck1:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, new_name):
        print("inside the setter")
        self.__name = new_name


if __name__ == "__main__":
    nathan = Duck("hong")
    fowl = Duck1('hong')
    print(nathan.hidden_name)
    print(fowl.__name)  # Duck1 멤버 변수에 접근 불가.
    # print(fowl._Duck1__name) # 의도적으로 접근은 가능하나 불필요
    # __은 클래스 정의를 외부에서 볼 수 없도록 속성에 대한 네이밍 컨벤션을 통해 숨길 수 있다.
