class Hanoi:
    def __init__(self, n):
        self.n = n
        self.towers = [range(n, 0, -1), [], []]
    
    def move_to(self, disk, start, end, by):
        #move disk - 1 to by through end
        print self.towers
        if disk > 1:
            self.move_to(disk - 1, start, by, end)

        #move disk from start to end
        val = self.towers[start].pop()
        self.towers[end].append(val)

        #move disk - 1 from by to end through start
        if disk > 1:
            self.move_to(disk - 1, by, end, start)

if __name__ == "__main__":
    n = 3
    h = Hanoi(n)
    h.move_to(n, 0, 2, 1)
    print h.towers
