class name:
    def __init__(self):
        print("inti")
    def fun(self):
        print(self)
        print("ad")
        pass

class name1(name):
    def fun(self):
        super(name1,self).fun()



a=name1()
a.fun()