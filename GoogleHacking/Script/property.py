# property
# 使调用类中的方法向引用类中的字段属性一样

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def stud_info(self):
        print(self.name, self.age)


stud = Student("felix", 12)
print(stud.stud_info)