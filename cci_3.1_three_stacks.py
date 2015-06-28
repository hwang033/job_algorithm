class stack:
    def __init__(self, length):
        self.length = length
        self.array = [0 for i in range(length)]
        self.tops = [0, length/3, length*2/3]

    def push(self, s_num, val):
        #check s_num stack is full or not
        if 3 > s_num >= 0 and self.tops[s_num] <= self.length*s_num/3:
            self.array[self.tops[s_num]] = val 
            self.tops[s_num] += 1
        print self.array
            
    def pop(self, s_num):
        #check s_num stack is empty or not 
        if 3 > s_num >= 0 and self.tops[s_num] > self.length*s_num/3: 
            val = self.array[self.tops[s_num] - 1]
            self.array[self.tops[s_num] - 1] = 0
            self.tops[s_num] -= 1
            print self.array
            return val
        else:
            return None

if __name__ == "__main__":
    s = stack(3)
    s.push(1, 1)
    s.push(1, 2)
    print s.pop(1)
    print s.pop(1)
    
    



