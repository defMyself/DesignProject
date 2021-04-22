class Cheese:
    def __init__(self, *args, **kwargs):
        # args -- tuple of
        # kwargs
        self.num_holes = kwargs.get('num_holes', random_holes())
