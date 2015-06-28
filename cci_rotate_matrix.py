def rotate_90(M):

    for i in range(len(M)/2):
        M[i], M[len(M) - i - 1] = M[len(M) - i - 1], M[i] 
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            M[i][j], M[j][i] = M[j][i], M[i][j]
    return M

if __name__ == "__main__":
   print rotate_90([[1,2,3],[4,5,6],[7,8,9]]) 
