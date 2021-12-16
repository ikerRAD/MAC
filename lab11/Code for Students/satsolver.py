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
    num_apariciones_iguales = [0]*(num+1)
    
    for clause in claus:
        for lit in clause:
            num_apariciones[abs(lit)] = num_apariciones[abs(lit)] + 1
            num_apariciones_iguales[abs(lit)] = num_apariciones_iguales[abs(lit)] + int(lit/abs(lit))
    
    for i in range(1, len(num_apariciones)):
        #si aparece una vez o todas sus apariciones son con el mismo signo
        if num_apariciones[i] == 1 or abs(num_apariciones_iguales[i]) == num_apariciones[i]:
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
    
    preproc_clauses, preproc_assignment = sat_preprocessing(num_variables, clauses, assignment)
    
    if preproc_clauses == []:
        return preproc_assignment
    elif preproc_clauses == ([[1], [-1]]):
        return "UNSATISFIABLE"
    
    #siempre estará a None
    lit = abs(preproc_clauses[0][0])
    true = 1
    false = 0
   
    #copiamos para no pasar valores por referencia
    assignment1 = copy(preproc_assignment)
    assignment1[lit] = true
    clauses1 = copyclauses(preproc_clauses)
    
    assignment2 = assignment
    assignment2[lit] = false
    clauses2 = clauses
    

    res1 = busqueda(num_variables, clauses1, assignment1)
        
    if res1 != "UNSATISFIABLE":
        return res1

    return busqueda(num_variables, clauses2, assignment2)

#conviene hacer preprocessing porque en el caso de sat no es muy costoso y siempre nos acercará más a la
#solución. Así que nos basaremos en hacer preprocessing y cuando el mismo se quede estancado, lo apoyaremos con alguna asignación
#abriendo un arbol. De esta manera también, nos encargamos de minimizar el arbol de búsqueda ya que en cada rama purgamos
#los efectos colaterales
def solve_SAT(num_variables, clauses):

   assignment = [None]*(num_variables+1)

   return busqueda(num_variables, clauses, assignment)


    


