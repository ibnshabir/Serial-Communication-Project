"""
    class A:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def calc(self):
            print('in A', end=": ")
            return self.x + self.y
    
    
    class B(A):
        def __init__(self, x, y, z):
            super().__init__(x,y)
            self.z =z
    
        def calc(self):
            print('in B', end=": ")
            return self.x + self.y + self.z
    
    
    if __name__ == "__main__":
        a = A(2, 3)
        b = B(3, 4, 5)
        print(a.calc())
        print(b.calc())
        # print(help(b))
"""


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_a(self):
        print(self.name, self.age)

class B(A):
    def __init__(self, name, age, school):
        self.school = school
        A.__init__(name, age)

    def print_b(self):
        print(self.school)


a = A('ali', 32)
a.print_a()
b = B('eesa', 1, 'home schooling')
b.print_b()

