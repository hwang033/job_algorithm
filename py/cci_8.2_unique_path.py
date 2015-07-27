import math

def unique_path(n, i=1, j=1):

    if i == n and j == n: 
        return 1

    if i > n or j > n: 
        return 0

    rst = unique_path(n, i+1, j) + unique_path(n, i, j+1)
    return rst

def unique_path_dp(n, m):
    if n < 2:
        return 1
    f = [0 for i in range(n)]
    f[0] = 1
    f[1] = 0
    for i in range(m):
        for j in range(1, n):
            f[j] = f[j-1] + f[j]
    return f[-1]

def unique_path_math(n, m):
    return math.factorial(n+m-2)/(math.factorial(m-1)*math.factorial(n-1))

if __name__ == "__main__":
    print unique_path(2)
    print unique_path_dp(2, 2)
    print unique_path_math(2, 2)
    
    
