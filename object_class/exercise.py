class Laser:

    def does():
        return 'disintegrate'

class Claw:

    def does():
        return 'crush'

class SmartPhone:
    
    def does():
        return 'ring'

class Robot:

    def __init__(self, laser, claw, smartPhone):
        self.laser = laser
        self.claw = claw
        self.smartPhone = smartPhone

    def dose(self):
        print(f"{self.laser} {self.claw} {self.smartPhone}")


if __name__ == "__main__":
    r1 = Robot(Laser.does(), Claw.does(), SmartPhone.does())
    r1.dose()