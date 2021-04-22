class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为: ", x.i)
print("MyClass 类的方法 f 输出为: ", x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = 0

    def __len__(self):
        return 10

    def speak(self):
        print("%s 说： 我 %d 岁。"%(self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()
print(len(p))