class MyHashSet:

    def __init__(self):
        self.numbs = []

    def add(self, key: int) -> None:
        if key not in self.numbs:
            self.numbs.append(key)

    def remove(self, key: int) -> None:
        if key in self.numbs:
            self.numbs.remove(key)

    def contains(self, key: int) -> bool:
        for i in self.numbs:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)