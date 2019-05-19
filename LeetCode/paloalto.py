class Random(object):
    def __init__(self, seed):
        self.seed = seed
        self.last = 0

    def random(self):
        self.last = (100000*self.last + 1000000) % self.seed
        return self.last
