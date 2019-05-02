from random import randint

class RspPlayer():
    player_num = 0

    def __init__(self, player_name):
        self.player = player_name

    def who_are(self):
        print(f"나는 {self.player_name}야")

    def select_rsp(self,rsp = ["가위", "바위", "보"]):
        player_rsp = rsp[randint(0, 2)]
        RspPlayer.player_num += 1
        return player_rsp
       
    @classmethod
    def total_player(cls):
        return f"총 참여자는 {RspPlayer.player_num}명"


if __name__ == "__main__":
    p1 = RspPlayer("나단")
    p2 = RspPlayer("명기")
    p3 = RspPlayer("병훈")
    print("p1 = "+ p1.select_rsp(), "p2 = " + p2.select_rsp(), "p3 = " + p3.select_rsp())
    
    
    print(RspPlayer.total_player())