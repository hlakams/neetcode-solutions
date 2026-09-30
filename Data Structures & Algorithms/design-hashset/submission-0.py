class MyHashSet:

    def __init__(self):
        # account for potential values 0 -> 1000000 inclusive
        self.hash_set = [False] * 1000001
        

    def add(self, key: int) -> None:
        self.hash_set[key] = True
        

    def remove(self, key: int) -> None:
        self.hash_set[key] = False
        

    def contains(self, key: int) -> bool:
        return True if self.hash_set[key] == True else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)