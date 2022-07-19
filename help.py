class Test():
    hi = 1

    def __init__(self):
        self.hih = Test.hi
        Test.hi *= -1
        print(Test.hi)


x = [ Test() for i in range(10000)]

y = 0

for i in x:
    y += i.hih
    print(y)
