def solveNQueens(n):
    res=[]
    def backtrack(r, cols, d1, d2, board):
        if r==n:
            res.append(board[:])
            return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2: continue
            backtrack(r+1, cols|{c}, d1|{r-c}, d2|{r+c},
                      board+[ "."*c+"Q"+"."*(n-c-1) ])
    backtrack(0,set(),set(),set(),[])
    return res
