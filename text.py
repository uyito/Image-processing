import numpy as np

def rowsum(matrix):
    """
    :param matrix (list): A list of lists where each inner list represents a row.
    :returns: (list) A list containing the sum of each row.
    """

    list_m = []
    for i in range(len(matrix)):
        add = 0
        for j in range(len(matrix[i])):
            add +=matrix[i][j]
        new = add
        list_m.append(new)
    return list_m

print(rowsum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))