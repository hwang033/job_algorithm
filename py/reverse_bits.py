class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = list(bin(n)[2:])
        while len(binary) < 32:
            binary.insert(0, '0')
        return int(''.join(binary[::-1]), 2)

if __name__ == "__main__":
    s = Solution()
    print s.reverseBits(1)
