from movimentacao import Movimentacao

class Logica():

    def bfs(self, puzzle_inicial):
        move = Movimentacao()

        end = str([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        count_estados_enf = 0 # guarda numero de estados 
        estados_visitados = [] 
        lista_estados = [[puzzle_inicial]] # lista_estados recebe os puzzles a serem verificados
        
        while lista_estados: # percorre todas as posições  

            caminho = lista_estados[0] #caminho guarda a largura explorada
            lista_estados = lista_estados[:0] + lista_estados[1:] #lista_estados passa a ter somente a largura não explorada
            final = caminho[-1] # recebe ultima estado da lista

            if final in estados_visitados: # se a ultima posiçao ja foi visitada volta pro inicio do while 
                continue
            for movimento in move.movimentos_possiveis(final): 
                if movimento in estados_visitados: # se o movimento ja passou por esse estado volta ao inicio do loop e vai para prox movimento 
                    continue
                lista_estados.append(caminho + [movimento]) 
            estados_visitados.append(final)# adiciono a lista de estados_visitados o ultimo estado do puzzle 
            count_estados_enf += 1 
            
            if final == end: 
                break 
        
        return caminho, count_estados_enf
