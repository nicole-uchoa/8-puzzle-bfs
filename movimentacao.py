class Movimentacao():
    
    def movimentos_possiveis(self, puzzle):
        movimentos = []
        linha = 0
        coluna = 0
        puzzle_list = eval(puzzle)
        # index do 0
        while 0 not in puzzle_list[linha]:linha += 1
        coluna = puzzle_list[linha].index(0) 
        
        #mover o 0 para baixo
        if linha<2:   
            movimentos = self.movimenta(linha, coluna, linha+1, coluna, movimentos, puzzle_list)      

        #mover o 0 para cima
        if linha>0:      
            movimentos = self.movimenta(linha, coluna, linha-1, coluna, movimentos, puzzle_list)   

        #mover o 0 para a direita
        if coluna<2:   
            movimentos = self.movimenta(linha, coluna, linha, coluna+1, movimentos, puzzle_list)      

        #mover o 0 para a esquerda
        if coluna>0:  
            movimentos = self.movimenta(linha, coluna, linha, coluna-1, movimentos, puzzle_list)      

        return movimentos

    def movimenta(self, linha1, coluna1, linha2, coluna2, movimentos, puzzle_list):
        puzzle_list[linha1][coluna1], puzzle_list[linha2][coluna2] = puzzle_list[linha2][coluna2], puzzle_list[linha1][coluna1] 
        movimentos.append(str(puzzle_list))
        puzzle_list[linha1][coluna1], puzzle_list[linha2][coluna2] = puzzle_list[linha2][coluna2], puzzle_list[linha1][coluna1]
        
        return movimentos