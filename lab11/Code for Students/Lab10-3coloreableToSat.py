from tools import list_minisat2list_our_sat
from time import time
from colour_tools import fromAdjacencyToGX, visualizeGXGraph
from satsolver import solve_SAT

def list2dimacs(my_list):
        return ('\n'.join(' '.join(map(str,sl)) for sl in my_list)) 



def calculate_num_clauses(graph):
    n_clauses = len(graph)*4
    aristas = 0
    #bucle que cuenta aristas
    for i in range(len(graph)-1):
        aristas += graph[i][i+1:].count(1)
        
    return n_clauses+aristas*3
    


# colores [r, g, b]  ([red, green, blue])
# Cuando el grafo tiene m nodos tu formula tiene 3xm variables.
# Dada la variable i, (i-1)/3 corresponde al nodo del grafo y (i-1)%3 al color  
def reduce_3colorable_to_SAT(graph):

   dimacs=[["p", "cnf", len(graph)*3, calculate_num_clauses(graph)]]
   
   #variables[id_variable][r = 0, g = 1, b = 2]
   variables = [[0,0,0] for i in range((len(graph)+1))]
   for i in range(len(graph)*3):
       variables[int(i/3)+1][i%3] = i+1
   
   #un color minimo por nodo 
   for i in range(len(graph)):
       dimacs.append([variables[i+1][0], variables[i+1][1], variables[i+1][2], 0])
   #un nodo no puede tener dos colores
   for i in range(1, len(graph)+1):
       dimacs.append([-variables[i][0], -variables[i][1], 0])
       dimacs.append([-variables[i][0], -variables[i][2], 0])
       dimacs.append([-variables[i][2], -variables[i][1], 0])
   #dos nodos conectados por una arista no pueden tener el mismo color    
   for i in range(len(graph)-1):
       for j in range(i+1, len(graph)):
           if graph[i][j]:
               dimacs.append([-variables[i+1][0], -variables[j+1][0], 0])
               dimacs.append([-variables[i+1][1], -variables[j+1][1], 0])
               dimacs.append([-variables[i+1][2], -variables[j+1][2], 0])
   return dimacs            
               
         
def test():   
     
    '''g1 = [[1, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 0],
          [0, 1, 0, 1]]
    
    f = open("g1.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g1)))
    f.close()
    # SATISFIABLE
    
    graph = fromAdjacencyToGX(g1)
    print(graph)
    visualizeGXGraph(graph, "g1.txt")

    
    g2 = [[1, 1, 1, 1],
          [1, 1, 0, 1],
          [1, 0, 1, 1],
          [1, 1, 1, 1]]
    
    f = open("g2.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g2)))
    f.close()
    # SATISFIABLE

    graph = fromAdjacencyToGX(g2)
    print(graph)
    visualizeGXGraph(graph, "g2.txt")
   

    g3 = [[1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 1, 1]]
    
    f = open("g3.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g3)))
    f.close()
    # UNSATISFIABLE
    
    graph = fromAdjacencyToGX(g3)
    print(graph)
    visualizeGXGraph(graph, "g3.txt")


    g4 = [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
    
    f = open("g4.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g4)))
    f.close()
    # UNSATISFIABLE
    
    graph = fromAdjacencyToGX(g4)
    print(graph)
    visualizeGXGraph(graph, "g4.txt")


    g5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    
    f = open("g5.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g5)))
    f.close()
    # UNSATISFIABLE
     
    graph = fromAdjacencyToGX(g5)
    print(graph)
    visualizeGXGraph(graph, "g5.txt")

    g6 = [[1, 1, 1, 0],
          [1, 1, 0, 1],
          [1, 0, 1, 1],
          [0, 1, 1, 1]]
    
    f = open("g6.txt", "w")
    f.write(list2dimacs(reduce_3colorable_to_SAT(g6)))
    f.close()
    # SATISFIABLE
    
    graph = fromAdjacencyToGX(g6)
    print(graph)
    visualizeGXGraph(graph, "g6.txt")'''
    
    tupla1 = list_minisat2list_our_sat ('g1.txt')
    tupla2 = list_minisat2list_our_sat ('g2.txt')    
    tupla3 = list_minisat2list_our_sat ('g3.txt')
    tupla4 = list_minisat2list_our_sat ('g4.txt')
    tupla5 = list_minisat2list_our_sat ('g5.txt')
    tupla6 = list_minisat2list_our_sat ('g6.txt')
    
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
    
    
test()
    
   
  