__author__ = 'kevinlu1010@qq.com'


class Receptionist:
    def __init__(self):
        self.observes = []
        self.status = ''

    def attach(self,observe):
        self.observes.append(observe)

    def notify(self):
        for observe in self.observes:
            observe.update()


class StockObserve:

    def __init__(self, name, receptionist):
        self.name = name
        self.receptionist = receptionist

    def update(self):
        print('%s,%s停止看股票'%(self.receptionist.status, self.name))


if __name__ == '__main__':
    receptionist = Receptionist()
    observe1 = StockObserve('张三', receptionist)
    observe2 = StockObserve('李四', receptionist)
    receptionist.attach(observe1)
    receptionist.attach(observe2)

    receptionist.status = '老板来了'
    receptionist.notify()

    receptionist.status = 'new news'
    receptionist.notify()