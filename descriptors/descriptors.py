class desc:
    def __get__(self, obj, type=None):
        print("hi from get")
        print(self)
        print(obj)
        print(type)
        return 10


class test1:
    attr1 = desc()

x = test1()
v = test1.attr1
print(v)

