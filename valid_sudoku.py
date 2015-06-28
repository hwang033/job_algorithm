class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        board = [[board[i][j] for j in range(9)] for i in range(9)]
    
        
        for i in range(9):
            if not self.is_valid_list(board[i]):
                return False
                
        for j in range(9):
            if not self.is_valid_list([board[i][j] for i in range(9)]):
                return False
        
        for k in range(9):
            l, c = divmod(k, 3)
            l *= 3
            c *= 3
            rec = board[l][c:c+3] + board[l + 1][c:c+3] + board[l + 2][c:c+3]
            if not self.is_valid_list(rec):
                return False
        return True

    def is_valid_list(self, s):
        num_hash = {}
        for num in s:
            if num != '.':
                if num < '1' or num > '9':
                    print "1", s
                    return False
                elif num_hash.has_key(num):
                    print "2", s
                    return False
                else:
                    num_hash[num] = 1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isValidSudoku([".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]) 
