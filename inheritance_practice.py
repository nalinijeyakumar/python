class Person():
    def __init__(self,name):
        self.name = name
    
    def hello(self):
        print("Hello",self.name)


p1 = Person("mike")
p1.hello()
class student(Person):
    def __init__(self, name,degree):
        super().__init__(name)
        self.degree = degree

s1 = student("Dave","CS")
s1.hello()


