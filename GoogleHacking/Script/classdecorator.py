class fruit:
    fruit_name = 'apple'

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def fruit_color(self):
        self.color = "red"
        print(self.color)

    @classmethod
    def fruit_info(cls):
        print('This is an %s'%cls.fruit_name)


fruit.fruit_info()
#fruit.fruit_color()