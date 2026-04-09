class A:
    def __init__(self,name):
        self.name=name
b=A("h")
b.g="hwllo"
print(b.__dict__)
c=A("name","dsfdf")
print(c.__dict__)