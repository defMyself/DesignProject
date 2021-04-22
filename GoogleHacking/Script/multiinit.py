import time


class Date:
    # main constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # optional
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday) # 返回一个构造器


a = Date(2012, 12, 21)
print(a.year, a.month, a.day)
b = Date.today()
print(b.year, b.month, b.day)
