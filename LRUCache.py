class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.usedcapacity = 0
        self.recentlyUsed = {}
        self.recentlyList = []
    # @return an integer

    def get(self, key):
    # @param key, an integer
    # @param value, an integer
    # @return nothing
        if self.recentlyUsed.has_key(key):
            self.recentlyList.remove(key)
            self.recentlyList.append(key)
            return self.recentlyUsed[key]
        else:
            return -1

    def set(self, key, value):
        #if reached capacity remove least recently used
        if self.usedcapacity >=  self.capacity:

            if self.recentlyUsed.has_key(key):
                self.recentlyList.remove(key)
            else:
                leastRecently = self.recentlyList[0]
                self.recentlyList.remove(leastRecently)
                self.recentlyUsed.pop(leastRecently)

            self.recentlyList.append(key)
            self.recentlyUsed[key] = value
        else:
            if self.recentlyUsed.has_key(key):
                self.recentlyList.remove(key)
                self.recentlyList.append(key)
            else:
                self.usedcapacity += 1
                self.recentlyList.append(key)
            self.recentlyUsed[key] = value

if __name__ == '__main__':
    lr = LRUCache(10)
    [lr.set(10,13),lr.set(3,17),lr.set(6,11),lr.set(10,5),lr.set(9,10),lr.get(13),lr.set(2,19),lr.get(2),lr.get(3),lr.set(5,25),lr.get(8),lr.set(9,22),lr.set(5,5),lr.set(1,30),lr.get(11),lr.set(9,12),lr.get(7),lr.get(    5),lr.get(8),lr.get(9),lr.set(4,30),lr.set(9,3),lr.get(9),lr.get(10),lr.get(10),lr.set(6,14),lr.set(3,1),lr.get(3),lr.set(10,11),lr.get(8),lr.set(2,14),lr.get(1),lr.get(5),lr.get(4),lr.set(11,4),lr.set(12,24),lr.set(5,18)    ,lr.get(13),lr.set(7,23),lr.get(8),lr.get(12),lr.set(3,27),lr.set(2,12),lr.get(5),lr.set(2,9),lr.set(13,4),lr.set(8,18),lr.set(1,7),lr.get(6),lr.set(9,29),lr.set(8,21),lr.get(5),lr.set(6,30),lr.set(1,12),lr.get(10),lr.set    (4,15),lr.set(7,22),lr.set(11,26),lr.set(8,17),lr.set(9,29),lr.get(5),lr.set(3,4),lr.set(11,30),lr.get(12),lr.set(4,29),lr.get(3),lr.get(9),lr.get(6),lr.set(3,4),lr.get(1),lr.get(10),lr.set(3,29),lr.set(10,28),lr.set(1    ,20),lr.set(11,13),lr.get(3),lr.set(3,12),lr.set(3,8),lr.set(10,9),lr.set(3,26),lr.get(8),lr.get(7),lr.get(5),lr.set(13,17),lr.set(2,27),lr.set(11,15),lr.get(12),lr.set(9,19),lr.set(2,15),lr.set(3,16),lr.get(1),lr.set(    12,17),lr.set(9,1),lr.set(6,19),lr.get(4),lr.get(5),lr.get(5),lr.set(8,1),lr.set(11,7),lr.set(5,2),lr.set(9,28),lr.get(1),lr.set(2,2),lr.set(7,4),lr.set(4,22),lr.set(7,24),lr.set(9,26),lr.set(13,28),lr.set(11,26)]
