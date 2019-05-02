class Char():
    
    def __init__(self, name):
        self.name = name
        self.power = 15
        self.level = 1
    
    def says(self):
        return f"i am {self.name}!"

    def status(self):
        return f"power: {self.power} level: {self.level}"


class CharChange(Char):

    def say(self):
        return f"i am {self.name}!"
    
    def status(self, power):
        self.power = power
        return f"power: {self.power} level: {self.level}"


def who_char(char):
    print(char.says())

if __name__ == "__main__":
    ch1 = Char("zilet")
    ch2 = Char("mutal")
    print(ch1.says()+ " and " + ch2.says())
    print(ch1.status(), ch2.status())
    ch1 = CharChange("marine")
    ch2 = CharChange("zerg")
    print(ch1.says()+ " and " + ch2.says())
    print(ch1.status(12), ch2.status(15))
    who_char(ch1)