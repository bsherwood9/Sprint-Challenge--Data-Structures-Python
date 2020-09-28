# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#         self.head = 0
#         self.tail = 1

#     def append(self, item):
#         if len(self.storage) < self.capacity:
#             self.storage.append(item)
#         if len(self.storage) == self.capacity:
#             self.storage.pop(self.head)
#             self.storage.insert(self.tail, item)
#             self.head += 1
#             self.tail += 1

#     def get(self):
#         return self.storage


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(self.capacity+1)]
        self.head = 0
        self.tail = 0

    def append(self, item):
        self.storage[self.head] = item
        self.head += 1
        if self.head == self.capacity:
            self.head = 0
        if self.head == self.tail:
            self.tail += 1
        if self.tail == self.capacity:
            self.tail = 0

    def get(self):
        if self.head == self.tail:
            return []
        return list(filter(lambda x: x != None, self.storage))


dog = RingBuffer(5)
dog.append(1)
dog.append(2)
dog.append(3)
dog.append(4)
dog.append(5)
dog.append(6)
dog.append(7)
print(dog.get())
