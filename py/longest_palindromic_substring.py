import pdb
class Solution:

    # @return a string
    '''
    def longestPalindrome(self, s):
        # f[i][j]= f[i-1][j-1] + (1 if s[i]==s[j] else 0) 
        m = len(s) 
        f = [[(1 if i==j else 0) for j in range(m)] for i in range(m)]
        #print f
        max_len = 0
        max_i = 0
        max_j = 0
        for i in range(m-1, -1, -1):
            for j in range(i+1, m, 1):
                if f[i+1][j-1] == 0:
                    if j - i == 1 and s[i] == s[j]:
                       f[i][j] = 2
                       if f[i][j] > max_len:
                           max_len, max_i, max_j = f[i][j], i, j
                    else:
                       f[i][j] = 0
                elif s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2
                    if f[i][j] > max_len:
                        max_len, max_i, max_j = f[i][j], i, j
                    #print f, max_len, max_i, max_j
                    
        return s[max_i:max_j+1]
    '''
    def longestPalindrome(self, s):
        if not s:
            return s
        char_pos = {}
        s_list = list(s)
        rst_len = 0
        rst = s_list[0]
        for idx, char in enumerate(s_list):
            char_pos.setdefault(char, [])
            char_pos[char].append(idx)
        
        for char, pos in char_pos.items():
            while pos:
                idx = pos.pop()
                for prev_idx in pos:
                    if idx - prev_idx + 1 > rst_len and self.is_palindrome(s_list[prev_idx: idx + 1]):
                        rst_len = idx - prev_idx + 1
                        rst = s[prev_idx: idx + 1]
        return rst
    
    def is_palindrome(self, s):
        return s == s[::-1]

def main():
    s = Solution()
    print s.longestPalindrome("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")                
    print s.longestPalindrome("accbac")                
    print s.longestPalindrome("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd")                
    print s.longestPalindrome("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu")                

if __name__ == "__main__":
    main()
