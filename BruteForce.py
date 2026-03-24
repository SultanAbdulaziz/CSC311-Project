#here


def bruteforce(s1:str ,s2:str):
    def generate_alignments(s: str,max_num_of_dashes: int,min_num_of_dashes: int,result_set: set):
        if max_num_of_dashes == min_num_of_dashes : return
        l = list(s)
        for i in range(len(l)+1):
            formattedstring = l.copy()
            formattedstring.insert(i,"-")
            result_set.add("".join(formattedstring))
            generate_alignments(formattedstring,max_num_of_dashes-1,min_num_of_dashes,result_set)
        
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

    if len(s1) > len(s2):
        s1combs = {s1}
        s2combs = set()
    else:
        s1combs = set()
        s2combs = {s2}
        
    min_num_of_dashes = max(len(s1),(len(s2)))
    max_num_of_dashes = len(s1)+len(s2)
    
    generate_alignments(s1,max_num_of_dashes,min_num_of_dashes,s1combs)
    generate_alignments(s2,max_num_of_dashes,min_num_of_dashes,s2combs)

    minimal_cost = 100000
    for sequence1 in s1combs:
        for sequence2 in s2combs:
            if(len(sequence1) == len(sequence2)):
                current_cost = alignment_cost(sequence1,sequence2) 
                if minimal_cost >= current_cost:
                    minimal_cost = current_cost
                    result = [sequence1,sequence2,minimal_cost]
            else: continue
    return result


s1 = input("enter first sequence1")
s2 = input("Enter Second sequence2")
try:
    result = bruteforce(s1,s2)
except Exception:
    print("Something went wrong")
