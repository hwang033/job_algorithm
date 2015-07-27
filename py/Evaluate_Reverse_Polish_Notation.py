#!/usr/bin/python

class Solution:
    # @param tokens, a list of Sting
    # @return an integer
    def evalRPN(self, tokens):
        tokens_l = []
        for s in tokens:
            try:
                tokens_l.append(float(s))
            except ValueError: 
                rst = 0
                if s == "+":
                    rst = tokens_l[-2] + tokens_l[-1]
                if s == "-":
                    rst = tokens_l[-2] - tokens_l[-1]
                if s == "*":
                    rst = tokens_l[-2] * tokens_l[-1]
                if s == "/":
                    rst = tokens_l[-2] / tokens_l[-1]
                tokens_l.pop()
                tokens_l.pop()
                tokens_l.append(rst)
                #print rst
        return int(tokens_l.pop())

if __name__ == "__main__":
    s = Solution()
    #print s.evalRPN(["4", "13", "5", "/", "+"])
    #print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print s.evalRPN(["4","13","5","/","+"])
            
