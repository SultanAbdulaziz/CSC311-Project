def alignment_cost(s1:str,s2:str):
        def scoring_function(c1:str, c2:str):
            alpha = 2
            beta = 1
            if c1 == "-" or c2 == "-": return beta
            elif c1 == c2: return 0
            else: return alpha
        
        cost = 0
        for i in range(len(s1)):
            cost += scoring_function(s1[i],s2[i])
        return cost

def DynamicProgramming(s1:str ,s2:str):
    w1,w2 = LCS(s1,s2)
    print(w1, w2)
    print(alignment_cost(w1,w2))
    
    


def LCS(s1:str,s2:str):
    m = len(s1)
    n = len(s2)
    c = [[0] * (n+1) for _ in range(m+1)] #tabulation
    for i in range(m):
        c[i][0] = 0
    for j in range(1,n):
        c[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    w1 = []
    w2 = []

    while n > 0 and m > 0:
        if s1[m-1] == s2[n-1]:
            w1.append(s1[m-1])
            w2.append(s2[n-1])
            n -= 1
            m -= 1
        elif c[m-1][n] > c[m][n-1]:
            m -= 1
            w1.append(s1[m])
            w2.append("-")
        else:
            n -= 1
            w1.append("-")
            w2.append(s2[n])
        
    while n > 0:
        n -= 1
        w1.append("-")
        w2.append(s2[n])
    while m > 0:
        m -= 1
        w1.append(s1[m])
        w2.append("-")
    
    return "".join(reversed(w1)), "".join(reversed(w2))


