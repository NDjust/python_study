class StatsList(list):
    '''
    list를 상속받는 슈퍼 클래스
    확장과 래핑을 사용.
    '''

    def sum(self):
        return sum(v for v in self)

    def count(self):
        return sum(1 for v in self)
     
    
    def mean(self):
        return self.sum() / self.count()

    def sum2(self):
        return sum(v ** 2 for v in self)

    def variance(self):
        return (self.sum2() / (self.sum()**2/self.count()) / (self.count() - 1))

    def stddev(self):
        import math
        return math.sqrt(self.variance())


if __name__ == "__main__":
    subset1 = StatsList([10, 6, 2, 13, 56])
    data = StatsList([14, 6, 4, 2, 10])
    data.extend(subset1)
    print(data)
    print(data.mean())
    print(data.sort())
    print(data[len(data) // 2])
    print(data.variance())