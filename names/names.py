import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1
lista = BSTNode(names_1[0])
for name in names_1[1:]:
    lista.insert(name)

for name in names_2:
    if lista.contains(name):
        duplicates.append(name)

# newSet = set(names_1).intersection(names_2)
# for i in newSet:
#     duplicates.append(i)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
