import pdb
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if not words or not L:
            return [""]
        
        i = total_len = 0
        line_word = []
        rst = []
        
        while i < len(words) :
            
            if len(words[i]) + total_len + len(line_word) <= L:
                #word[i] + prev words + sapce
                line_word.append(words[i])
                total_len += len(words[i])
                i += 1
            else: 
                pdb.set_trace()
                subrst = ""
                if len(line_word) == 1:
                    subrst += line_word[0] + " "*(L - total_len)
                elif len(line_word) == 2:
                    subrst += line_word[0] + " "*(L - total_len) + line_word[1]
                else:
                    div, mod = divmod(L - total_len, len(line_word) - 1)

                    for idx in xrange(len(line_word)):
                        if idx == 0:
                            subrst += line_word[idx]
                        elif mod > 2 :
                            subrst += " "*(div + 2) + line_word[idx]
                            mod -= 2
                        elif mod <= 2 and mod > 0:
                            subrst += " "*(div + 1) + line_word[idx]
                            mod -= 1
                        else:
                            subrst += " "*(div) + line_word[idx]
                rst.append(subrst)
                total_len = 0
                line_word = []
        
        subrst = ' '.join(line_word)
        subrst += ' '*(L - len(subrst))
        rst.append(subrst)

        return rst               

if __name__ == "__main__":            
    s = Solution()
    print s.fullJustify(["What","must","be","shall","be."], 12)
    print s.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
    print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
