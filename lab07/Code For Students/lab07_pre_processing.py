 

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
        # TODO
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

    

def test():
    assert ([], [None, 1]) == sat_preprocessing(1, [[1]], [None, None])
    
    
    assert ([[1],[-1]]) == sat_preprocessing(1, [[1], [-1]], [None,None])[0]
    
    
    ans = sat_preprocessing(4, [[4], [-3, -1], [3, -4, 2, 1], [1, -3, 4],
                                         [-1, -3, -4, 2], [4, 3, 1, 2], [4, 3],
                                         [1, 3, -4], [3, -4, 1], [-1]], [None, None, None, None, None])
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][4] == 1
    
    
    ans = sat_preprocessing(5, [[4, -2], [-1, -2], [1], [-4],
                                [5, 1, 4, -2, 3], [-1, 2, 3, 5],
                                [-3, -1], [-4], [4, -1, 2]], 
                                  [None, None, None, None, None, None])
    assert ans[0] == [[1],[-1]]            
    
    
    ans = sat_preprocessing(6, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4]], 
                                   [None, None, None, None, None, None, None])
    assert ans[0] == [[5, 6, 2, 4], [3, 5, 2, 4], [-5, 2, 3], [-3, 2, -5, 6, -4]]
    assert ans[1][1] == 1
    
    
    ans = sat_preprocessing(7, [[-5, 3, 2, 6, 1], [5, 6, 2, 4],
                                [3, 5, 2, -1, 4], [1], [2, 1, 4, 3, 6],
                                [-1, -5, 2, 3], [-3, 2, -5, 6, -4, 7]], 
                                   [None, None, None, None, None, None, None, None] )
    assert ans[0] == []
    assert ans[1][1] == 1
    assert ans[1][4] == 1
    assert ans[1][6] == 1
    assert ans[1][7] == 1
    
   
    ans = sat_preprocessing(6, [[-6, -4, 5, -1, ], [1,2,3,6,-5],
                                [4,6], [-4, -3], [-1],
                                [1,6,-5,-4], [3,5,-6,-5,-1]],
                                   [None, None, None, None, None, None, None])
    assert ans[0] == []
    assert ans[1][1] == 0
    assert ans[1][2] == 1
    assert ans[1][3] == 0
    assert ans[1][5] == 0
    assert ans[1][6] == 1   
   
test()
