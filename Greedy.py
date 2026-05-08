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
            """if alpha <= beta:
                S1_result.append(S1[i])
                S2_result.append(S2[j])
                total_cost += alpha
                i += 1
                j += 1
            else:"""
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