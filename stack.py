class Stack:
    def __init__(self, limit):
        self.stack = []
        self.limit = limit
    
    def size(self):
        return len(self.stack)
    
    def queue(self, item):
        if(self.size() <= self.limit):
            self.stack.append(item)

    def dequeue(self):
        if(self.size() > 0):
            return self.stack.pop()
        else:
            return None