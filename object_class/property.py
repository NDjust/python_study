class Duck:
    def __init__(self, name):
        self.hidden_name = name

    def get_name(self):
        print("inside the getter")
        return self.hidden_name

    def set_name(self, new_name):
        print("inside the setter")
        self.hidden_name = new_name

    name = property(get_name, set_name)


class Duck1:
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


class Circle:

    def __init__(self, raidus):
        self.radius = raidus

    @property
    def diameter(self):
        return 2 * self.radius


class Game:
    def __init__(self, correct_num):
        self.hidden_correct = correct_num

    def get_correct(self):
        print("output correct_num")
        return self.hidden_correct

    def set_correct(self, new_num):
        print("reset correct num")
        self.hidden_correct = new_num

    num = property(get_correct, set_correct)


class Game1:
    def __init__(self, correct_num):
        self.hidden_correct = correct_num

    @property
    def correct(self):
        print("output correct_num")
        return self.hidden_correct

    @correct.setter
    def correct(self, new_num):
        print("reset correct num")
        self.hidden_correct = new_num


if __name__ == "__main__":
    d1 = Duck1('duck')
    print(d1.name)
    d1.name = '오리'
    print(d1.name)

