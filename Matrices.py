import copy


class Matrix:
    def __init__(self, rows, columns, tab=None):
        if tab == None:
            self.tab = [[0 for a in range(columns)] for i in range(rows)]
        else :
            self.tab = tab
        # on aura N le nombre de lignes et M le nombre de colonnes
        self.columns = columns
        self.rows = rows
    
    """
    We define a Matrix by the number of rows M and columns N
    """
    def __add__(self, B):
        assert self.columns == B.columns and self.rows == B.rows  
        self.tab = [[self.tab[i][a] + B.tab[i][a] for a in range(self.rows)] for i in range(self.columns)]
        return self.tab

    def __sub__(self, B):
        assert self.columns == B.columns and self.rows == B.rows  
        self.tab = [[self.tab[i][a] - B.tab[i][a] for a in range(self.rows)] for i in range(self.columns)]
        return self.tab

    def __mul__(self, B):
        assert self.columns == B.rows
        matrice = [[0 for a in range(B.columns)] for i in range(self.rows)]
        for r in range(len(matrice)):
            for i in range(B.columns):
                for col in range(len(matrice)):
                    matrice[r][i] += (self.tab[r][col]*B.tab[col][i])
        return self.__class__(self.rows, B.columns, matrice)

    def isIdentite(self):
        assert self.columns == self.rows
        for i in range(len(self.tab)):
            if self.tab[i][i] != 1:
                return False
            else:
                for elt in range(len(self.tab[i])):
                    if elt == i:
                        pass
                    elif self.tab[i][elt] != 0:
                        return False
        return True

    def isCarre(self):
        return self.columns == self.rows


    def determinant(self):
        # ad - bc
        assert self.isCarre() == True
        if self.rows == 3:
            det = 0
            for i in range(1,4):
                det = det + (((-1)**(1+i)) * (self.tab[0][i-1]) * (self.co_matrix(i).determinant_2_b_2()))
            print(det)
            return det
        else:
            __det = 0 
            for i in range(1,self.columns+1):
                print(self.co_matrix(i))
                __det = __det + (((-1)**(1+i)) * (self.tab[0][i-1]) * (self.co_matrix(i).determinant()))
            return __det

    def determinant_2_b_2(self):
        return ((self.tab[0][0] * self.tab[1][1]) - (self.tab[0][1] * self.tab[1][0]))


    def co_matrix(self,n):
        assert self.isCarre() == True
        assert n > 0
        co_tab = copy.deepcopy(self.tab)
        co_tab.pop(0)
        for i in range(len(co_tab)):
            co_tab[i].pop(n-1)
        return self.__class__(self.rows-1, self.columns-1, co_tab)

    def __repr__(self):
        return f'{self.tab}'





A = Matrix(3, 3, [[1,2,3],[4,10,0],[3,2,1]])
B = Matrix(3, 2, [[2,1],[3,7],[3,9]])

C = Matrix(2,2, [[1,2],
                    [3,4]])
                    
D = Matrix(3, 3, [[2,1,1],[3,7,3],[3,9,4]])
E = Matrix(5, 5, [[0,1,4,5,7],[0,0,3,15,0],[0,0,0,4,9],[2,6,0,5,0],[5,0,67,0,1]])


print(D-A)