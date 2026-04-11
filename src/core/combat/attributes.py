

class Attributes:
    def __init__(self, user):
        self.base     = user.job.data['stats']
        self.received = { 'hp': 0, 'str': 0, 'dex': 0, 'knw': 0, 'lky': 0, 'res': 0 }
        self.main     = { }
        for keys in self.received:
            self.main[keys] = self.base[keys] + self.received[keys]