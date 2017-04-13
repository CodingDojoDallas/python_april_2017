class MathDojo(object):
    def __init__(self):
        self.number = 0
        pass

    def add(self, *number):
        for i in number:
            if type(i) is list:
                for x in i:
                    self.number += x
            else:
                self.number += i
        return self

    def sub(self, *number):
        for i in number:
            if type(i) is list:
                for d in i:
                    self.number -= d
            else:
                self.number -= i
        return self

    def result(self):
        print self.number

math = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).sub(2, [2,3], [1.1, 2.3]).result()
