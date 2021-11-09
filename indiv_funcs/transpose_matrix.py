'''
11-9-21
imran iftikar

this program will attempt to take a TWO DIMENSIONAL matrix in the form of:

        array = [
        [a1, a2, a3, ..., aN],
        [b1, b2, b3, ..., bN],
        [c1, c2, c3, ..., cN],
        ...,
        [z1, z2, z3, ..., zN],
    ]

and will return its transpose. 

log.txt separate. 

known bugs:
    none

'''

######### dependencies

'''none'''

######### funcs

def get_col(matrix_2d, _index):
    return list(row[_index] for row in matrix_2d) # O(n)

def transpose(matrix):

    new_array = [get_col(matrix, i) for i in range(len(matrix[0]))] # O(n) and nested O(n), becomes O(n**2)
    return new_array
   
######### vars

m1 = [
    [7,7],
    [5,2],
    [3,1],
    [4,5]
]

######### main

print(transpose(m1))