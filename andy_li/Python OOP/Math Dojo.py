class MathDojo(object):
    def __init__(self, *int):
        self.result = 0

    def add(self, *args):
        # print args
        if len(args) < 1:
            print "Please enter at least 1 argument."
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for elem in arg:
                    self.result += elem
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        # print args
        if len(args) < 1:
            print "Please enter at least 1 argument."
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for elem in arg:
                    self.result -= elem
            else:
                self.result -= arg
        return self

    def display(self):
        print self.result
        return self



md = MathDojo()
print md.add(3, [1, 3], (3, 1)).subtract(3, [1], (1, 2)).result
