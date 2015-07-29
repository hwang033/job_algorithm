import pdb
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return 
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            board[i] = [x for x in board[i]]
        g = set()
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    g.add((i, j))
        
        finished = set()
        
        for x in g:
            if x not in finished:
                print x 
                pdb.set_trace()
                stack = []
                flag = True
                stack.append(x)
                fill = []
                while stack:
                    cur_i, cur_j = stack.pop()
                    coord = zip([cur_i - 1, cur_i + 1, cur_i, cur_i], [cur_j, cur_j, cur_j - 1, cur_j + 1])
                    for i, j in coord:
                        if i < 0 or i >= m or j < 0 or j >= n:
                            flag = False
                        else:
                            if board[i][j] == "O" and (i, j) not in finished:
                                stack.append((i, j))
                    
                    finished.add((cur_i, cur_j))
                    fill.append((cur_i, cur_j))
                
                if flag:
                    for i, j in fill:
                        board[i][j] = 'X'

                print board    
        for i in xrange(m):
            board[i] = ''.join(board[i])

if __name__ == "__main__":
    s = Solution()
    b = ["OXO","XOX","OXO"]
    #b = ["XOX","XOX","XOX"]
    #b = ["XXXX", "XOOX", "XXOX", "XOXX"]
    s.solve(b)

    print b
