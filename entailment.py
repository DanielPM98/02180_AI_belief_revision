from sympy.logic.boolalg import to_cnf, Or, And, Not
from itertools import combinations
import sympy



def entailment(belief_base, prop):
    clauses = []
    
    for belief in belief_base:
        b_cnf = to_cnf(belief.proposition)
        if isinstance(b_cnf, And):
            clauses += list(b_cnf.args)
        else:
            clauses.append(b_cnf)
   
    clauses += [to_cnf(~prop)]

    result = set()
    #result = []
    while True:
        print("clauses", clauses)
        pairs = list(combinations(clauses,2))
        print('Pairs: ', pairs)
        #res_new = []
        for i,j in pairs:
            temp = pl_resolve(i,j)
            if False in temp:
                print('WHYYYY')
                return True
            # if len(temp) != 0:
            #     res_new.append(temp)
            result = result.union(set(temp))

        # result = [item for sublist in res_new for item in sublist]
        # result = list(set(result))

        if result.issubset(set(clauses)):
            return False
        # if all(x in clauses for x in result):
        #     print('FALSE BITCHES')
        #     return False
     
        for element in result:
            if element not in clauses:
                clauses.append(element)



def pl_resolve(left, right):
    result = []
    
    left_syms = dissociate(left)
    right_syms = dissociate(right)

    resultant = []
    for ls in left_syms:
        for rs in right_syms:
            if ls == ~rs or ~ls == rs:
                resultant = _remove_sym(ls, left_syms) + _remove_sym(rs, right_syms)

                resultant = list(set(resultant))

                if len(resultant) == 0:
                    result.append(False)
                elif len(resultant) == 1:
                    result.append(resultant[0])
                else:
                    result.append(Or(*resultant))

    return result
    

def dissociate(x):
    if len(list(x.args)) < 2:
        out = [x]
    else:
        out = list(x.args)
    return out


def _remove_sym(sym, clause):
    return [s for s in clause if s != sym]

def recombine(pairs):
    for i in range(len(pairs)):
        if isinstance(pairs,list):
            if len(pairs[i])>1:
                x=0
                while x < len(pairs[i])-1:
                    
                    pairs[i][0]=Or(pairs[i][0], pairs[i][x+1])
                    
                    x+=1
                pairs[i]=pairs[i][0]
            else:
                pairs[i]=pairs[i][0]

    return pairs


def singles(clauses):
    
    for i in range(len(clauses)-1):
        x=0
        
        while x <= len(clauses)-1:
            if i==x:
                pass
            else:
                if isinstance(clauses[i],str) or isinstance(clauses[x],str):
                    pass
                else:
                    if clauses[i]==~clauses[x]:
                        clauses[i]="rem"
                        clauses[x]="rem"
                    else:
                        pass
            x+=1
        x=0
        while x <= len(clauses)-1:
            if i==x:
                pass
            else:
                if isinstance(clauses[i],str) or isinstance(clauses[x],str):
                    pass
                else:
                    if clauses[i]==~clauses[x]:
                        clauses[i]="rem"
                        clauses[x]="rem"

                    elif clauses[i]==clauses[x]:
                        clauses[x]="rem"
                        
                    else:
                        pass
            x+=1
    count=1
    for i in clauses:
        
        if i=="rem":
            
            count+=1
    for i in range(count-1):
        clauses.remove("rem")
    return clauses
