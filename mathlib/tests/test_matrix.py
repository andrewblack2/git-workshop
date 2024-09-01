from mathlib import Matrix

def test_matrix_addition():
    matrix1 = Matrix(data=[[1, 2], [3, 4]])
    matrix2 = Matrix(data=[[5, 6], [7, 8]])
    result = matrix1 + matrix2
    assert result.data == [[6, 8], [10, 12]]

def test_matrix_transpose():
    matrix1 = Matrix(data=[[1, 2], [3, 4], [5, 6]])
    matrix1.transpose()
    assert matrix1.data == [[1, 3, 5], [2, 4, 6]]

# TODO: ALL - Implement tests for all other Matrix methods
# Use the test_matrix_addition test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html
