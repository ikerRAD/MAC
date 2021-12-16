from random import choice

def falseClause(clauses, num_variables, assignment):
    
    for clause in clauses:
        good = False
        for lit in clause:
            if lit<0:
                if assignment[-lit] == 0:
                    good = True
                    break
            else:
                if assignment[lit] == 1:
                    good = True
                    break
        if not good:
            return clause
    return []
                

def random_3SAT (clauses, num_variables):
    assignment = [None] + [choice([0,1]) for n in range(num_variables)]
    
    for i in range(1, num_variables+1):
        false_clause = falseClause(clauses, num_variables, assignment)
        if not false_clause:
            return "SAT"
        else:
            tochange = choice(false_clause)
            assignment[abs(tochange)] = (assignment[abs(tochange)] + 1)%2
    return "UNSAT"


#Por mi cuenta, para probar el lema
def lema(clauses, num_variables):
    n = int(10 * pow(1.5, num_variables)) + 1
    for i in range(n):
        resp = random_3SAT(clauses, num_variables)
        if resp == "SAT":
            return resp
    return resp


def test():
    
   
    clauses = [[1, -2, -4], [1, 4, 2], [2, -1, -4], [2, 4, -1], [-3, -1, 4], [-3, 1, -2], [-3, -4, 2]]
    print("Esta instancia es SAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 4))
    print("Probando el lema:")
    print(lema(clauses, 4))

    
    clauses = [[3, 1, 2], [1, 2, -3],[-3, 1, -2], [1, 3, -2],
               [3, -1, 2], [-1, 2, -3],[-3, -1, -2], [-1, 4, -2]]
    
    print("Esta instancia es SAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 4))
    print("Probando el lema:")
    print(lema(clauses, 4))

    clauses = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    
    print("Esta instancia es SAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 3))
    print("Probando el lema:")
    print(lema(clauses, 3))
    
    clauses = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    
    print("Esta instancia es SAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 3))
    print("Probando el lema:")
    print(lema(clauses, 3))
    

    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    
    print("Esta instancia es UNSAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 3))
    print("Probando el lema:")
    print(lema(clauses, 3))
    
     
    clauses = [[4, -18, 19],[3, 18, -5],[-5, -8, -15],[-20, 7, -16],[10, -13, -7],
               [-12, -9, 17],[17, 19, 5],[-16, 9, 15], [11, -5, -14],[18, -10, 13],
               [-3, 11, 12],[-6, -17, -8],[-18, 14, 1],[-19, -15, 10],[12, 18, -19],
               [-8, 4, 7],[-8, -9, 4],[7, 17, -15],[12, -7, -14],[-10, -11, 8],
               [2, -15, -11],[9, 6, 1],[-11, 20, -17],[9, -15, 13],[12, -7, -17],
               [-18, -2, 20],[20, 12, 4],[19, 11, 14],[-16, 18, -4],[-1, -17, -19],
               [-13, 15, 10],[-12, -14, -13],[12, -14, -7],[-7, 16, 10],[6, 10, 7],
               [20, 14, -16],[-19, 17, 11],[-7, 1, -20],[-5, 12, 15],[-4, -9, -13],
               [12, -11, -7],[-5, 19, -8],[-16],[20, -14, -15],[13, -4, 10],
               [14, 7, 10],[-5, 9, 20],[10, 1, -19],[-16, -15, -1],[16, 3, -11],
               [-15, -10, 4],[4, -15, -3],[-10, -16, 11],[-8, 12, -5],[14, -6, 12],
               [1, 6, 11],[-13, -5, -1],[-12],[1, -20, 19],[-2, -13, -8],
               [18],[-11, 14, 9],[-6, -15, -2],[-5],[-6, 17, 5],
               [-13, 5, -19],[20, -1, 14],[9, -17, 15],[-5, 19, -18],[-12, 8, -10],
               [-18, 14, -4],[15, -9, 13],[9, -5, -1],[10, -19, -14],[20, 9, 4],
               [-9, -2, 19],[-5, 13, -17],[2, -10, -18],[-18, 3, 11],[7, -9, 17],
               [-15, -6, -3],[-2, 3, -13],[12, 3, -2],[2, -2, -3, 17],[20, -15, -16],
               [-5, -17, -19],[-20, -18, 11],[-9, 1, -5],[-19, 9, 17],[17],[1],
               [4, -16, -5]]
    
    print("Esta instancia es UNSAT. El algoritmo random devuelve:")
    print(random_3SAT(clauses, 20))
    print("Probando el lema:")
    print(lema(clauses, 20))
    
   
    
test()    
       

