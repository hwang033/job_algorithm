class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        rst = 0
        print tokens
        for t in tokens:
            print t, stack 
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == '+':
                    rst = n1 + n2
                elif t == '-':
                    rst = n2 - n1
                elif t == '*':
                    rst = n1*n2
                else:
                    rst = n2/n1
                
                stack.append(rst)

        return stack[-1]

if __name__ == "__main__":                
    s = Solution()
    print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
