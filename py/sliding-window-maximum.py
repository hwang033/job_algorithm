class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        
        rst = []
        max_heap = nums[:k]
        self.buildHeap(max_heap)
        for i in range(k, len(nums)):
            rst.append(max_heap[0])
            #print max_heap
            max_heap[0] = nums[i]
            self.heapify(max_heap, 0)
        
        return rst
        
    
    def buildHeap(self, heap_l):
        length = len(heap_l)
        
        for i in range(length/2, -1, -1):
            self.heapify(heap_l, i)
        
    
    def heapify(self, heap_l, i):
        largest = i
        if 2*i < len(heap_l) and heap_l[2*i] > heap_l[largest]:
            largest = 2*i
            
        if 2*i + 1 < len(heap_l) and heap_l[2*i+1] > heap_l[largest]:
            largest = 2*i + 1
    
        if largest != i:
            heap_l[largest], heap_l[i] = heap_l[i], heap_l[largest]
            self.heapify(heap_l, largest)
   
if __name__ == "__main__":
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
