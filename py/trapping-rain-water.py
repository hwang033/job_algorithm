class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        # stack 
        if not A:
            return 0
            
        stack = [A[0]]
        water = 0
        
        for i in xrange(1, len(A)):
            print stack

            sub_rst = [A[i]] 
            
            while len(stack) != 0 and stack[-1] < A[i]:
                sub_rst.append(stack.pop())
            
            if len(sub_rst) > 1:

                if len(stack) != 0:
                    sub_rst.append(stack.pop())

                flag = min(sub_rst[-1],sub_rst[0])

                if not (len(stack) == 0 and flag == 0):
                    for j in xrange(len(sub_rst) - 1, -1, -1):
                        x = sub_rst[j]
                        if flag >= x:
                            water += (flag - x)
                            stack.append(flag)
                        else:
                            if j != 0  and j != len(sub_rst) - 1:
                                flag = x
                            stack.append(x)
                else:
                    stack.append(A[i])

            else:
                stack.append(A[i])
            
        return water    
            
if __name__ == "__main__":
    s = Solution()

    print s.trap([6,0,0,2,8,9,2,6,5,0,0,9,7,0,4,7,3])
    print s.trap([4,2,3])
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print s.trap([4,7,7,5,3,3,4,9,5,8,6,2,0,6,2,7,4])
