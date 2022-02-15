from matriz import Matriz
from logica_bfs import Logica
m = Matriz()
l = Logica() 

#puzzle = m.gera_matriz_aleatória()

puzzle = str([[1, 5, 2], 
          [8, 6, 3],
          [7, 0, 4]])

while m.check_ideal(puzzle) == False:
    # checar se a matriz tem solução
    if m.check_tem_solucao(puzzle):
        count_mov = 0
        caminho, count_est_enfileirado = l.bfs(puzzle)
        for puzzle in caminho:
            puzzle = eval(puzzle)
            print('\n')
            m.print_matriz(puzzle)
            count_mov += 1

            m.check_ideal(puzzle)

        print ("\nNumeros de estados enfileirados: ", count_est_enfileirado)
        print (count_mov-1," movimentos\n\n")

    else:
        print("\nPuzzle não tem solução!\n")  
        break  
