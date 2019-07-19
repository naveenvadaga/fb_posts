class name:
    a = "string"

    def __init__(self):
        pass

    # print("inti")

    def fun(self):
        print(self)
        print("ad")
        pass

    def af(self):
        print("1")
        print(name.a)


class name1(name):
    a = "adsf"

    def fun(self):
        name.a = "change"


a = name1()
a.fun()
a.af()
print("2")
print(a.a)
