class Parent1:
    def parent_info(self):
        print("This is parent 1 info class.")
#Base class 2
class Parent2:
    def parent_info_two(self):
        print("This is parent two info class.")
#derived class...
class Child(Parent1, Parent2): #multiple inheritance
    pass
obj1 = Child()
obj1.parent_info()
obj1.parent_info_two()
