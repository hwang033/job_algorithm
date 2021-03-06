import pdb
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        #dynimic programming
        #if s[i] == ')': f[i][j] = f[i+1][j]
        #if s[i] == '(':
        #   if s[j] == ')' and (j + 1 - i) % 2 == 0: f[i][j] = max(f[i+1][j-1], f[i+1][j], f[i][j-1]) + 1
        #   else: f[i][j] = f[i][j-1]
        if not s:
            return 0


        f = [0 for i in range(len(s))]
        stack = []
        stack_idx = []
        #pdb.set_trace() 

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                stack_idx.append(i)
            else:
                if len(stack) != 0: 
                    stack.pop()
                    idx = stack_idx.pop()
                    f[i] = 1
                    f[idx] = 1
        maxsum = 0
        sum = 0
        for x in f:                
            if x == 0:
                maxsum = (sum if sum > maxsum else maxsum)
                sum = 0
            else:
                sum += 1

        maxsum = (sum if sum > maxsum else maxsum)
        return maxsum 

if __name__ == "__main__":
    s = Solution()
    #input = ['(()', ')()())', '((()()()))']
    input = ['((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))']
    for x in input:
        print x
        print s.longestValidParentheses(x)
