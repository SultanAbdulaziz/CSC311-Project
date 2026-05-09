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

# Greedy Alignment
def greedy_alignment(S1, S2):

    S1_result = []
    S2_result = []
    
    i = 0
    j = 0
    while i < len(S1) and j < len(S2):
        if S1[i] == S2[j]:
            S1_result.append(S1[i])
            S2_result.append(S2[j])
            i += 1
            j += 1
        else:
            if i + 1 < len(S1) and S1[i+1] == S2[j]:
                S1_result.append(S1[i])
                S2_result.append('-')
                i += 1
            else:
                S1_result.append('-')
                S2_result.append(S2[j])
                j += 1
                

    while i < len(S1):
        S1_result.append(S1[i])
        S2_result.append('-')
        i += 1

    while j < len(S2):
        S1_result.append('-')
        S2_result.append(S2[j])
        j += 1

    return "".join(S1_result), "".join(S2_result)

def Greedy(s1:str ,s2:str):
    w1,w2 = greedy_alignment(s1,s2)
    print(w1, w2)
    print(alignment_cost(w1,w2))

