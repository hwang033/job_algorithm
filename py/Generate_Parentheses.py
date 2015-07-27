#!/usr/lib/python

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        #trackback
        rst = []
        self.generatePar(rst, "", [], n)
        return rst
    
    def generatePar(self, rst, subrst, stack, n):
        
        if len(subrst) ==  2*n and not stack:
            rst.append(subrst)
            return
        if len(subrst) >= 2*n:
            return 
        
        if not stack:
            stack.append("(")
            subrst += "("
            self.generatePar(rst, subrst, stack[:], n)
        else:
            # if add ")", stack.pop()
            # if add "(", stack.append() 
            stack.pop()
            self.generatePar(rst, subrst + ")", stack[:], n)
            
            stack.append("(")
            stack.append("(")
            self.generatePar(rst, subrst + "(", stack[:], n)

if __name__ == "__main__":
    
    s = Solution()
    print s.generateParenthesis(2)
