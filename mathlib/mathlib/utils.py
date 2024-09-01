def validate_matrix(matrix):
    """
    Validates if the input is a well-formed matrix (2D list with consistent row lengths).
    :param matrix: 2D list representing the matrix.
    :return: True if valid, raises ValueError otherwise.
    """
    # Person 4 - Implement matrix validation logic
    if (type(matrix.data)) == list and (type(matrix.data[0]) == list):
        raise ValueError("Invalid matrix form")
    
    size = len(matrix.data[0])
    for row in matrix:
        if len(row) != size:
            raise ValueError("Row lengths are not consistent")

def check_dimensions(matrix1, matrix2):
    """
    Checks if two matrices can be added or multiplied.
    :param matrix1: First matrix (2D list).
    :param matrix2: Second matrix (2D list).
    :return: True if dimensions are compatible, raises ValueError otherwise.
    """
    # TODO: Person 4 - Implement dimension check logic
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrix dimensions are not compatable")

def identity_matrix(size):
    """
    Creates an identity matrix of the given size.
    :param size: The number of rows/columns for the identity matrix.
    :return: Identity matrix as a 2D list.
    """
    base = []
    for i in range(size):
        row = [0] * size
        row[i] = 1
        base.append(row)

    return base

def zero_matrix(rows, cols):
    """
    Creates a zero matrix with the given dimensions.
    :param rows: Number of rows.
    :param cols: Number of columns.
    :return: Zero matrix as a 2D list.
    """
    base = []
    for i in range(rows):
        row = [0] * cols
        base.append(row)

    return base

def minor(matrix, row, col):
    """
    Calculates the minor of a matrix by removing the specified row and column.
    :param matrix: 2D list representing the matrix.
    :param row: The row to remove.
    :param col: The column to remove.
    :return: The minor matrix as a 2D list.
    """
    base = []
    for r in matrix:
        row = []
        for c in row:
            if r == row or c == col:
                row.append(matrix.data[r][c])

        base.append(row)

    return base

def cofactor(matrix):
    """
    Calculates the cofactor matrix of a given matrix.
    :param matrix: 2D list representing the matrix.
    :return: Cofactor matrix as a 2D list.
    """
    base = []
    for r in matrix:
        row = []
        for c in row:
            if r == row or c == col:
                row.append(matrix.data[r][c])

        base.append(row)

    return base

