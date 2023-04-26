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
        if type(B) == int or type(B) == float:
            matrice = [[0 for a in range(self.columns)] for i in range(self.rows)]
            for r in range(len(matrice)):
                for i in range(self.columns):
                    for col in range(len(matrice)):
                        matrice[r][i] = self.tab[r][i] * B
            return self.__class__(self.rows, self.columns, matrice)
        elif type(B) == Matrix:
            assert self.columns == B.rows
            matrice = [[0 for a in range(B.columns)] for i in range(self.rows)]
            for r in range(len(matrice)):
                for i in range(B.columns):
                    for col in range(len(matrice[0])):
                        matrice[r][i] += (self.tab[r][col]*B.tab[col][i])
                        #result[r][i] += A[r][col] * B[col][i]
            return self.__class__(self.rows, B.columns, matrice)

    def __pow__(self, p):
        for i in range(p-1):
            self *= self
        return self



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

    def isReversible(self):
        return self.determinant() != 0

    def isCarre(self):
        return self.columns == self.rows


    def determinant(self):
        # ad - bc
        assert self.isCarre() == True
        if self.rows == 2:
            return self.determinant_2_b_2()
        elif self.rows == 3:
            det = 0
            for i in range(1,4):
                det = det + (((-1)**(1+i)) * (self.tab[0][i-1]) * (self.co_factor(i).determinant_2_b_2()))
            return det
        else:
            __det = 0 
            for i in range(1,self.columns+1):
                print(self.co_factor(i))
                __det = __det + (((-1)**(1+i)) * (self.tab[0][i-1]) * (self.co_factor(i).determinant()))
            return __det

    def determinant_2_b_2(self):
        return ((self.tab[0][0] * self.tab[1][1]) - (self.tab[0][1] * self.tab[1][0]))


    def co_factor(self,n, row=1):
        # only for 3x3 Matrix or bigger
        assert self.isCarre() == True
        #assert n >= 3
        co_tab = copy.deepcopy(self.tab)
        co_tab.pop(row-1)
        for i in range(len(co_tab)):
            co_tab[i].pop(n-1)
        return self.__class__(self.rows-1, self.columns-1, co_tab)

    def get_comatrix(self):
        #chaque element est le determinant du cofacteur a l'indice a,i
        if self.rows == 2:
            return self.__class__(self.rows, self.columns, [[self.tab[1][1],self.tab[1][0]*-1],[self.tab[0][1]*-1,self.tab[0][0]]])
        else:
            new_tab = [[(self.co_factor(a, i).determinant())*((-1)**(a+i)) for a in range(1, self.columns+1)] for i in range(1, self.rows+1)]
            return self.__class__(self.rows, self.columns, new_tab)
        
    
    def transpose(self):
        tab_trans = [[self.tab[i][j] for i in range(self.rows)] for j in range(self.columns)]
        return self.__class__(self.rows, self.columns, tab_trans)

    def inverse(self):
        assert self.isReversible() == True
        print(self.get_comatrix().transpose())
        tab_inverse = self.get_comatrix().transpose() * (1/self.determinant())
        return Matrix(self.rows, self.columns, tab_inverse)

    def __repr__(self):
        return f'{self.tab}'

