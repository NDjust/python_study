class Mutal:
    def __init__(self):
        self.now_state = "mutal"
        self.hp = 100
        self.attackt_rate = 10

    @property
    def state(self):
        print("now state")
        return self.now_state

    @state.setter
    def state(self, select, upgrade=["gardian", 'devaurer']):
        print("upgrade complete")
        self.now_state = upgrade[select]
def hello():
    print("hi")


if __name__ == "__main__":
    h1 = Mutal()
    print(h1.state)
    h1.state = 1
    print(h1.state)


class user:

    def __init__(self):
        self.level = 1
        self.power = 15
        print("유저 생성!")