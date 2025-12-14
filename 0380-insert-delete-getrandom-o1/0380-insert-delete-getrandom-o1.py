class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.choices = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.choices.append(val)
            self.hashmap[val] = len(self.choices)-1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            if self.hashmap[val] == len(self.choices):
                self.choices.pop()
                del self.hashmap[val]
                return True
            else:
                VC = self.hashmap[val]
                self.hashmap[self.choices[-1]] = VC
                self.choices[VC] = self.choices[-1]
                self.choices.pop()
                del self.hashmap[val]
                return True
        else:
            return False


    def getRandom(self) -> int:
        print(self.choices)
        print(self.hashmap)
        return random.choice(self.choices)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()