'''
imran iftikar
11-6-21

multiplication of two of any size 2d array in the form

    array = [
        [a1, a2, a3, ..., aN],
        [b1, b2, b3, ..., bN],
        [c1, c2, c3, ..., cN],
        ...,
        [z1, z2, z3, ..., zN],
    ]

i dont care too much about time, as this is mainly a personal project for fun, but I'll be keeping time in mind,
as its an area I feel like I need to improve in. even though im not going to try to optimize for speed, 
I'm going to keep track of everything major to see if I get the time right, as I might not
and then ill just get feedback on where i will likely get it wrong

log.txt separate. 

known bugs:
none as of now

'''

######### Dependencies

'''cant use any, i'm gonna try to do this vanilla'''


######### Funcs

def multip_1row(row1, row2):

    if len(row1) == len(row2):
        return sum(list(row1[element]*row2[element] for element in range(len(row1)))) # O(n) n is length of row
    else:
        raise ValueError("The dimensions are incomplete")

def get_col(matrix_2d, _index):
    return list(row[_index] for row in matrix_2d) # O(n)

def multiply_matrix(matrix1, matrix2):

    # matrix1 row and column number. len() is O(1), constant time
    matrix1_rows = len(matrix1) # just taking the first. I assume that each argument is a completely filled list

    # matrix2 row and column number. still constant time
    matrix2_cols = len(matrix2[0])

    if matrix1_rows == matrix2_cols:
        new_matrix = []

        # overall O(n**4) i believe. kinda sucks, but at least it should (just tested, it does indeed) work
        for m1_row in matrix1: # i believe this line alone is O(n)
            new_matrix_row = []
            for _index in range(len(matrix2[0])): # this line is O(n)
                new_matrix_row.append(multip_1row( # this line is O(n**2)
                    m1_row,
                    get_col(matrix2, _index)
                ))
            new_matrix.append(new_matrix_row)
        
        return new_matrix

    else:
        raise ValueError("The dimensions of the arrays passed as \
        arguments are incompatible and cannot be multiplied")


######### vars

m1 = [
    [4,8,2],
    [1,4,2]
]

m2 = [
    [3,6],
    [1,4],
    [9,8]
]

######### main

print(multiply_matrix(m1, m2))




