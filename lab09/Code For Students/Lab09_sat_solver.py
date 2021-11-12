from time import time
from tools import list_minisat2list_our_sat
      
def solitaria(claus, assign):
    modif = False
    for clause in claus:
        if len(clause) == 1:
            lit = clause[0]
            if assign[abs(lit)] == None:
                modif = True
                if lit<0:
                    assign[-lit] = 0
                else:
                    assign[lit] = 1
    return modif

def unica(num, claus, assign):
    modif = False
    num_apariciones = [0]*(num+1)
    
    for clause in claus:
        for lit in clause:
            num_apariciones[abs(lit)] = num_apariciones[abs(lit)] + 1
    
    for i in range(1, len(num_apariciones)):
        if num_apariciones[i] == 1:
            #buscamos la aparición y cambiamos los valores
            for clause in claus:
                if -i in clause:
                    if assign[i] == None:
                        modif = True
                        assign[i] = 0
                    break
                elif i in clause:
                    if assign[i] == None:
                        modif = True
                        assign[i] = 1
                    break    
    return modif


def borrarTrue(claus, assign):
    modif = False
    toRemove = []
    
    for clause in claus:
        for lit in clause:
            #Si en una clausula está el literal y su negado
            if (-lit) in clause:
                toRemove.append(clause)
                break
            #si hay un valor asignado
            if assign[abs(lit)] != None:
                #Si hace true la fórmula
                if (assign[abs(lit)] == 0 and lit < 0) or (assign[abs(lit)] == 1 and lit > 0):
                    #añadimos para no alterar el ciclo del for
                    toRemove.append(clause)
                    break
               
    #eliminamos lo que sea true
    if toRemove:
        modif = True
        for removed in toRemove:
            claus.remove(removed)
            
    return modif


def eliminarLiterales(num, claus, assign):
    modif = False
    for clause in claus:
        #preparamos array para eliminar para no alterar los bucles
        toRemove = []
        for i in range(len(clause)):
            #If the literal has a value assigned
            if assign[abs(clause[i])] != None:
                #Si el literal es false en la clausula, lo borramos de ella
                if (clause[i] < 0 and assign[-clause[i]] == 1) or (clause[i] > 0 and assign[clause[i]] == 0):
                    toRemove.append(clause[i])
        
        if toRemove:
            modif = True
            for removed in toRemove:
                clause.remove(removed)
    
    return modif



def sat_preprocessing(num_variables, clauses, assignment):

    
    update = True
    while update and [] not in clauses:
        update = False   
        # Si hay cláusula formada por una sola variable, hacerla true
        update = update or solitaria(clauses, assignment)
        # Si una variable sale solo una vez, hacerla true
        update = update or unica(num_variables, clauses, assignment)
        #eliminar clausulas true
        update = update or borrarTrue(clauses, assignment)
        #Eliminar literales ya asignados que se vuelvan false
        update = update or eliminarLiterales(num_variables, clauses, assignment)

        if [] in clauses:
            
            return ([[1], [-1]], assignment)
        else:
            if (clauses == []) or (not update):
                     return (clauses, assignment)  
                 
                    
def copy(m):
    ret = [0]*len(m)
    for i in range(len(m)):
        ret[i] = m[i]
    return ret
	
def copyclauses(m):
    ret=[]
    for clause in range(len(m)):
        ret.append(copy(m[clause]))
    return ret


def busqueda(num_variables, clauses, assignment):
    #buscamos el primer literal no asignado
    lit = -1
    true = 1
    false = 0
        
    for clause in clauses:
        for litt in clause:
            if assignment[abs(litt)] == None:
                lit = abs(litt)
                if litt<0:
                    true = 0
                    false = 1
                break
        if lit != -1:
            break
    
        
    #si todo está asignado
    if(lit == -1):
        return "UNSATISFIABLE"
    
    #copiamos para no pasar valores por referencia
    assignment1 = copy(assignment)
    assignment1[lit] = true
    clauses1 = copyclauses(clauses)
    
    assignment2 = copy(assignment)
    assignment2[lit] = false
    clauses2 = copyclauses(clauses)
    
    #una vez hecho un cambio, preprocesamos por si ha habido 'daños colaterales'
    #ya que el preproceso es rápido y solo efectua movimientos correctos dependiendo del contexto
    
    p_clauses, p_assign = sat_preprocessing(num_variables, clauses1, assignment1)
    
    #vemos que tal nos ha ido
    if not p_clauses:
        return p_assign
    #si no nos ha ido bien pero tampoco mal, seguimos por la misma rama
    elif p_clauses != ([[1], [-1]]):
        res1 = busqueda(num_variables, p_clauses, p_assign)
    #si nos ha ido mal ponemos res1 a unsatifiable
    else:
        res1 = "UNSATISFIABLE"
        
    #vemos que hay en res1, si es distinto de UNSATISFIABLE, es una solución
    if res1 != "UNSATISFIABLE":
        return res1
    
    #si llegamos aquí es que la rama anterior no tiene solución así que seguimos por la
    #segunda rama

    p_clauses, p_assign = sat_preprocessing(num_variables, clauses2, assignment2)
    
    #volvemos a ver que tal de la misma manera
    if not p_clauses:
        return p_assign
    
    elif p_clauses != ([[1], [-1]]):
        return busqueda(num_variables, p_clauses, p_assign)
    else:
        return "UNSATISFIABLE"
    
#conviene hacer preprocessing porque en el caso de sat no es muy costoso y siempre nos acercará más a la
#solución. Así que nos basaremos en hacer preprocessing y cuando el mismo se quede estancado, lo apoyaremos con alguna asignación
#abriendo un arbol. De esta manera también, nos encargamos de minimizar el arbol de búsqueda ya que en cada rama purgamos
#los efectos colaterales
def solve_SAT(num_variables, clauses):

   assignment = [None]*(num_variables+1)
   proc_clauses, proc_assign = sat_preprocessing(num_variables, clauses, assignment)
   if not proc_clauses:
       return proc_assign
   elif proc_clauses == ([[1], [-1]]):
       return "UNSATISFIABLE"
   else:
       return busqueda(num_variables, proc_clauses, proc_assign)


    
def test():
    ## Para probar el juego de pruebas
    '''tupla1 = list_minisat2list_our_sat ('instancias/1-unsat.cnf')
    tupla2 = list_minisat2list_our_sat ('instancias/2-sat.cnf')    
    tupla3 = list_minisat2list_our_sat ('instancias/3-sat.cnf')
    tupla4 = list_minisat2list_our_sat ('instancias/4-sat.cnf')
    tupla5 = list_minisat2list_our_sat ('instancias/5-unsat.cnf')
    tupla6 = list_minisat2list_our_sat ('instancias/6-unsat.cnf')
    tupla7 = list_minisat2list_our_sat ('instancias/7-unsat.cnf')
    tupla8 = list_minisat2list_our_sat ('instancias/8-unsat.cnf')
    tupla9 = list_minisat2list_our_sat ('instancias/9-unsat.cnf')
    tupla10 = list_minisat2list_our_sat ('instancias/10-unsat.cnf')
    
    start_time = time()
    print(solve_SAT(tupla1[0], tupla1[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 1 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla2[0], tupla2[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 2 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla3[0], tupla3[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 3 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla4[0], tupla4[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 4 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla5[0], tupla5[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 5 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla6[0], tupla6[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 6 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla7[0], tupla7[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 7 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla8[0], tupla8[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 8 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla9[0], tupla9[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 9 : %0.10f seconds." % elapsed_time) 
    
    start_time = time()
    print(solve_SAT(tupla10[0], tupla10[1]))
    elapsed_time = time() - start_time   
    print("Elapsed time 10 : %0.10f seconds." % elapsed_time) '''
    
    clauses = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    solutions = [[0, 0, 0, 0],
                 [0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0],
                 [None, None, 0, 0], #no se contemplaba en el material y es solución válida
                 [None, 0, 0, 0],
                 [None, 0, 1, 1],
                 [None, 1, 0, 0],
                 [None, 1, 1, 0]]
    assert solve_SAT(3,clauses) in solutions
    
    
    clauses = [[1, -2, -3], [2, -3, 1], [3, -2, 1],
               [2, 3, 1]]
    solutions = [[0, 1, 0, 0], 
                 [0, 1, 0, 1], 
                 [0, 1, 1, 0], 
                 [0, 1, 1, 1], 
                 [1, 1, 0, 0], 
                 [1, 1, 0, 1], 
                 [1, 1, 1, 0], 
                 [1, 1, 1, 1],
                 [None, 1, 0, 0], 
                 [None, 1, 0, 1], 
                 [None, 1, 1, 0], 
                 [None, 1, 1, 1],
                 [None, 1, None, None]]
    assert solve_SAT(3,clauses) in solutions
    

    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    assert solve_SAT(3,clauses) == "UNSATISFIABLE"
    
     
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
    assert solve_SAT(20, clauses) == "UNSATISFIABLE" 
    
    print("Tests passed") 
   
    clauses = [[-6, -4, -2, 6], [-5], [7], [1, -3], 
               [1, -4, -1, -7], [-6, -1], [1], [-7]]
    
    assert solve_SAT(7, clauses) == "UNSATISFIABLE" 

    
    
    
    

test()

