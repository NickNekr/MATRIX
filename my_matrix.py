from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1_, matrix2_):
        self.matrix1 = matrix1_
        self.matrix2 = matrix2_


class Matrix(object):
    def __init__(self, lines):
        self.lines = deepcopy(lines)

    def __eq__(self, other):
        if self.lines == other.lines:
            return True
        else:
            return False

    def __str__(self):
        return '\n'.join('\t'.join(list(map(str, line)))
                         for line in self.lines)

    def tr(self):
        ans = 0
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if i == j:
                    ans += self.lines[i][j]
        return ans

    def transpose(self):
        self.lines = [[i[j] for i in self.lines]
                      for j in range(len(self.lines[0]))]
        return Matrix(self.lines)

    def transposed(self):
        return Matrix([[i[j] for i in self.lines]
                       for j in range(len(self.lines[0]))])

    def size(self):
        return len(self.lines), len(self.lines[0])

    def __add__(self, other):
        other_lines = []
        if self.size() == other.size():
            for i, j in zip(self.lines, other.lines):
                other_lines.append([sum(i) for i in zip(i, j)])
            return Matrix(other_lines)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other_matrix = []
            for i in self.lines:
                other_matrix.append([j * other for j in i])
            return Matrix(other_matrix)
        elif isinstance(other, Matrix):
            if self.size()[1] == other.size()[0]:
                other_matrix = [[0 for i in range(len(other.lines[0]))]
                                for j in range(len(self.lines))]
                for els in range(len(other_matrix)):
                    for el in range(len(other_matrix[els])):
                        other_matrix[els][el] = sum([i * j[el]
                                                     for i, j in zip(self.lines[els],
                                                                     other.lines)])
                return Matrix(other_matrix)
            else:
                raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

    def __pow__(self, power):
        if power == 0:
            E = [[0 for i in range(len(self.lines[0]))]
                 for j in range(len(self.lines))]
            for i in range(len(E)):
                E[i][i] = 1
            return Matrix(E)
        elif power % 2 == 0:
            return Matrix((self * self).lines).__pow__(power // 2)
        else:
            return self * \
                   Matrix((self * self).lines).__pow__((power - 1) // 2)
        
        
        def stepped(self):
        matrix_slau = self.lines[:]
        zero = [0 for i in range(len(matrix_slau[0]))]
        for i in range(len(matrix_slau)):
            matrix_slau = matrix_slau[:i] + \
                          sorted(matrix_slau[i:],
                                 key=lambda x: x[i] == 0)
            if matrix_slau[i][i] != 0:
                matrix_slau[i] = list(map(lambda x: round(x, 3),
                                          map(lambda x: x * float((1 /
                                                                   matrix_slau[i][i])),
                                              matrix_slau[i])))
            for j in range(i + 1, len(matrix_slau)):
                matrix_slau[j] = list(map(lambda x: round(x, 3), [j + i for j, i in
                                                                  zip(matrix_slau[j],
                                                                      map(
                                                                          lambda x:
                                                                          x * ((-1) *
                                                                               matrix_slau[j][i]),
                                                                          matrix_slau[i]))]))
        for i in range(len(matrix_slau) - 1, 0, -1):
            for j in range(0, i):
                matrix_slau[j] = list(map(lambda x: round(x, 3), [j + i for j, i in
                                                                  zip(map(lambda x: x * (-1) * matrix_slau[j][i],
                                                                          matrix_slau[i]), matrix_slau[j])]))
        if isinstance(self, No_Tex_matrix):
            return No_Tex_matrix(matrix_slau)
        else:
            return Matrix(matrix_slau)
