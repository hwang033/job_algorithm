def fastLongestPalindromes(seq):
    """
    Behaves identically to naiveLongestPalindrome (see below), but
    runs in linear time.
    """
    seqLen = len(seq)
    l = []
    i = 0
    palLen = 0
    while i < seqLen:
        if i > palLen and seq[i - palLen - 1] == seq[i]:
            palLen += 2
            i += 1
            continue
        l.append(palLen)
        s = len(l) - 2
        e = s - palLen
        for j in xrange(s, e, -1):
            d = j - e - 1
            if l[j] == d: # *
                palLen = d
                break

            l.append(min(d, l[j]))
        else:
            palLen = 1
            i += 1
    l.append(palLen)
    lLen = len(l)
    s = lLen - 2
    e = s - (2 * seqLen + 1 - lLen)
    for i in xrange(s, e, -1):
        d = i - e - 1
        l.append(min(d, l[i]))
    
    max_l_i = max(list(enumerate(l)), key=lambda x: x[1])
    i = max_l_i[0]
    s = i // 2 - l[i] // 2
    return seq[s: (s+l[i])]

def main():
    seq = "accbbccaac"
    print  fastLongestPalindromes(seq)                
    #max_l_i = max(list(enumerate(l)), key=lambda x: x[1])
    #i = max_l_i[0]
    #s = i // 2 - l[i] // 2
    #print seq[s: (s+l[i])], s, l[i]
    #for i in range(len(seq)):
    #    s = i // 2 - l[i] // 2
    #    print seq[s: (s+l[i])], s, l[i]
    print fastLongestPalindromes("abac")                
    #print fastLongestPalindromes("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd")                
    #print fastLongestPalindromes("flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjugfohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflrezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuoronrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdegnlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtqghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvgdmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvynljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsawtimnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu")                

if __name__ == "__main__":
    main()
