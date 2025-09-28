class Test:
    def __init__(self):
        self.n = 0

    def my_func(self, num):
        self.num = 5
        print(num)
        print(self.num)

    def shownum(self):
        print(self.num)

t = Test()
t.my_func(Test().n)
t.shownum()