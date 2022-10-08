''' 
Program to perform basic matrix operations on a 2x2 Matrix
Author: Augusto Escudero
'''

from random import randrange

def vector_add(vector1, vector2):
    result = [vector1[0]+vector2[0], vector1[1] + vector2[1]]
    return result

def vector_mult(vector, scalar):
    result = []
    for item in vector:
        item*=scalar
        result.append(item)
    return result

class Matrix2x2():

    def __init__(self, row1, row2):
        self.r1c1 = row1[0]
        self.r1c2 = row1[1]
        self.r2c1 = row2[0]
        self.r2c2 = row2[1]

    def __str__(self):
        return (f"| {self.r1c1} {self.r1c2} |\n| {self.r2c1} {self.r2c2} |\n")
    
    def __eq__(self, matrix) -> bool:
        if matrix==None:
            return False
        return (self.r1c1 == matrix.r1c1 and self.r1c2 == matrix.r1c2 and self.r2c1 == matrix.r2c1 and self.r2c2 == matrix.r2c2)

def matrix_add(matrix_1, matrix_2):
    a = matrix_1.r1c1
    b = matrix_1.r1c2
    c = matrix_1.r2c1
    d = matrix_1.r2c2
    e = matrix_2.r1c1
    f = matrix_2.r1c2
    g = matrix_2.r2c1
    h = matrix_2.r2c2
    resultant_matrix = Matrix2x2([a+e, b+f], [c+g, d+h])
    return resultant_matrix

def matrix_inverse(matrix):
    a, b, c, d = matrix.r1c1, matrix.r1c2, matrix.r2c1, matrix.r2c2
    denominator = (a*d - b*c)
    if denominator==0:
        return None
    scalar = 1/(a*d - b*c)
    c1 = vector_mult([d, c*-1], scalar)
    c2 = vector_mult([b*-1, a], scalar)
    resultant_matrix = Matrix2x2([c1[0],c2[0]], [c1[1], c2[1]])
    return resultant_matrix

def matrix_product(matrix_1, matrix_2):
    a = matrix_1.r1c1
    b = matrix_1.r1c2
    c = matrix_1.r2c1
    d = matrix_1.r2c2
    e = matrix_2.r1c1
    f = matrix_2.r1c2
    g = matrix_2.r2c1
    h = matrix_2.r2c2
    resultant_vec_column_1 = vector_add(vector_mult([a,c], e), vector_mult([b,d], g))
    resultant_vec_column_2 = vector_add(vector_mult([a,c], f), vector_mult([b,d], h))
    resultant_matrix = Matrix2x2([resultant_vec_column_1[0], resultant_vec_column_1[1]], [resultant_vec_column_2[0], resultant_vec_column_2[1]])
    return resultant_matrix

