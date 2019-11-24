class Memory:
    def __init__(self, limit):
        self.limit = limit
        self.content = [0] * self.limit

    def save(self, address, data):
        self.content[address] = data

    def load(self, address):
        return self.content[address]