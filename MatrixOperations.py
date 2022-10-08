
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

A = Matrix2x2([0,1], [0,0])
B = Matrix2x2([1,0], [0,0])
C = Matrix2x2([1,3], [2,4])
AB = matrix_product(A,B)
BA = matrix_product(B,A)

D = Matrix2x2([1,1], [0,1])
E = Matrix2x2([-1,-1], [0,-1])

zero_matrix = Matrix2x2([0,0], [0,0])

test = Matrix2x2([9,2], [4,3])

print(matrix_inverse(test))

'''
count = 0
while True:
    if matrix_product(C,C) == zero_matrix:
        print(f"Found match after {count} iterations!")
        print(C)
        break
    else:
        a = randrange(10)
        b = randrange(10)
        c = randrange(10)
        d = randrange(10)
        C.r1c1, C.r1c2, C.r2c1, C.r2c2 = a, b, c, d
        count+=1


count = 0
D_inv = matrix_inverse(D)
E_inv = matrix_inverse(E)
E_plus_D_inv = matrix_inverse(matrix_add(E,D))

while True:
    if D_inv != None and E_inv != None and E_plus_D_inv == None:
        print(f"Found match after {count} iterations!")
        print("D:")
        print(D)
        print("D inverse:")
        print(D_inv)
        print("E:")
        print(E)
        print("E inv:")
        print(E_inv)
        print("E + D:")
        print(matrix_add(E,D))
        break
    else:
        a = randrange(10)
        b = randrange(10)
        c = randrange(10)
        d = randrange(10)
        e = randrange(10)
        f = randrange(10)
        g = randrange(10)
        h = randrange(10)
        D.r1c1, D.r1c2, D.r2c1, D.r2c2 = a, b, c, d
        E.r1c1, E.r1c2, E.r2c1, E.r2c2 = e, f, g, h
        count+=1
        print(f"Iteration: {count}")

'''
#print(matrix_product(C,C) == zero_matrix)

'''
print("AB:")
print(AB)
print("BA:")
print(BA)
'''
