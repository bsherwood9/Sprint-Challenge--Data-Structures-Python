class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.head = 0
        self.tail = 1

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.storage.pop(self.head)
            self.storage.insert(self.tail, item)
            self.head += 1
            self.tail += 1

    def get(self):
        return self.storage


dog = RingBuffer(5)
dog.append(1)
dog.append(2)
dog.append(3)
dog.append(4)
dog.append(5)
dog.append(6)
dog.append(7)
print(dog.get())
