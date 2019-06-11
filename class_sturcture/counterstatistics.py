'''
확장 : COUNTER객체 정의에서 통계 연산 처리 추가.

감싸기(래핑): Counter 객체를 지금 필요한 기능을 제공하는다른 클래스로 감싸는 기법. 이때 파이썬의 중요한 일부분에 해당하는 메소드들이 외부로 노출 될 수 있다.

연산처리 설계

1) 즉시(eager) 계산 : 가급적 조기에 계산을 수행. 그리고 계산된 값은 클래스 속성에 저장. 데이터 컬렉션에 변경이 가해지면
기존에 계산해놓은 값이 쓸모없어지는 단점이 있음.

2) 지연(lazy) 계산 : 메소드나 프로퍼티에 의해 요구될 때 비로소 계산하는 방식. 

'''
from collections import Counter
import math

class CounterStatistics:

    
    def __init__(self, raw_counter:Counter):
        self.raw_counter = raw_counter
        #인수로써 제공되는 Counter 객체는 CounterStatistics의 일부로서 저장된다.
        self.mean = self.compute_mean()
        self.steddv = self.compute_stddev()

    def compute_mean(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += value ** frequency
            count += frequency
        return total / count
    
    def compute_stddev(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency ** (value - self.mean) ** 2
            count += frequency
        return math.sqrt(total / (count - 1)