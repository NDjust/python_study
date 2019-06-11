'''
예제 카지노 패.

패는 두가지 부분으로 구성
- 카드들
- 베팅 금액

__slots__로 객체 최적화.
Refernece -  python cookbook

일반적으로 객체에 포함되는 속성의 개수는 동적으로 변경될 수 있다.
그리고 각 속성의 값도 역시 동적으로 바뀔 수 있다.

반면에 tuple 클래스를 기반으로 하는 객체는 변경 불가능하다.

여기서 살펴볼 것은 속성의 개수는 정해져 있지만 속서의 값은 변경할 수 있는 객체다.
속성의 개수가 고정되기 때문에 메모리와 처리시간에서도 이득이 있다.
'''
from collections import namedtuple
Card = namedtuple('Card', ('rank', 'suit')) 

class Hand:
    __slots__ = ('hand', 'bet')

    def __init__(self, bet, hand=None):
        self.hand = hand or []
        self.bet = bet

    def deal(self, card):
        self.hand.append(card)

    def __repr__(self):
        return "{class_}({bet}, {hand})".format(class_ = self.__class__, bet=self.bet, hand=self.hand)



if __name__ == "__main__":
    h1 = Hand(2)
    h1.deal(Card(rank=4, suit="clover"))
    h1.deal(Card(rank=8, suit="Heart"))
    h1.bet *= 2
    print(h1)
    #<class '__main__.Hand'>(4, [Card(rank=4, suit='clover'), Card(rank=8, suit='Heart')])
    Card.some_other_attribute = True # 정상 작동
    h1.some_other_attribute = True # Error 
    #-> __slots__를 사용해 새로운 속성 객체를 추가할 수 없게 설정하였기 때문.
