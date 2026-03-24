def bruteforce(s1:str ,s2:str):

    #this generates all possible alignments by adding a "-" each call then recursively call it self back until dashes left to be added = 0
    #min num of dashes to add is of length of the longer sequence 
    #max num of dashes is the sum of length of 2 sequences so we dont have "-" aligned with another "-"
    max_num_of_dashes = len(s1) + len(s2)
    min_num_of_dashes = abs(len(s2)-len(s1))
    def generate_alignments(s: str,num_of_dashes: int,result_set: set):
        if num_of_dashes == max_num_of_dashes+1: return
        l = list(s)
        for i in range(len(l)+1):
            formattedstring = l.copy()
            formattedstring.insert(i,"-")
            if num_of_dashes >= min_num_of_dashes: result_set.add("".join(formattedstring))
            generate_alignments(formattedstring,num_of_dashes+1,result_set)

    #this calculates the total cost of alignemt between 2 sequences by comparing each char
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
    #include the longer one only in the combinations since we need them to be of the same length the shorter one must have at leat one "-" so we dont add the original sequence itself
    if len(s1) > len(s2):
        s1combs = {s1}
        s2combs = set()
    elif len(s1) == len(s2):
        s1combs = {s1}
        s2combs = {s2}
    else:
        s1combs = set()
        s2combs = {s2}
    
    generate_alignments(s1,1,s1combs)
    generate_alignments(s2,1,s2combs)
    minimal_cost = 100000
    result = ["error","no alignment",0]

    for sequence1 in s1combs:
        for sequence2 in s2combs:
            if(len(sequence1) == len(sequence2)):
                current_cost = alignment_cost(sequence1,sequence2) 
                if minimal_cost >= current_cost:
                    minimal_cost = current_cost
                    result = [sequence1,sequence2,minimal_cost]
            else: continue
    return result 


s1 = input("Enter First sequence:   ")
s2 = input("Enter Second sequence:  ")
try:
    result = bruteforce(s1,s2)
    print(result[0])
    print(result[1])
    print("Cost : ",result[2])
except Exception as e:
    print("Something went wrong")
    print(e)

