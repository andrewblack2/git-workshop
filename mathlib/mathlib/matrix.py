import numpy as np

class Matrix:
    """
    A class to represent a matrix.
    """

    data: list[list[float]]

    def __init__(self, data: list[list[float]]):
        """
        Constructs all the necessary attributes for the matrix object.
        """
        self.data = data

    def __str__(self):
        """
        String representation of the matrix.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


    def __add__(self, other):
        """
        Add two matrices together.
        """
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions to be added.")

        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))])


    def __mul__(self, other):
        """
        Multiply a matrix by a scalar.
        """
        return Matrix([[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))])


    # TODO: Person 1 - Implement matrix outer product (__matmul__)
    def __matmul__(self, other):
        """
        Compute the outer product of two matrices
        """
        # check dimensions
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise
        
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] *= other.data[i][j]
    
        return Matrix(self.data)
        


    def transpose(self):
        """
        Transpose function for Matrix
        """
        n = len(self.data)
        m = len(self.data[0])
        self.data = [[self.data[i][j] for i in range(n)] for j in range(m)]

    # TODO: Person 1 & 2 - Implement determinant calculation (determinant)
    # Either code together or have one person code and the other review
    # If coding together, use pair programming & co-author the commit (git commit -m "message" -m "Co-authored-by: name <email>")
    # If reviewing, leave comments on what you think can be improved
    def determinant(self):
        """
        calculating the determinant of a matrix
        """
        if(len(self.data) != len(self.data[0])):
            raise ValueError("Matrix must be square")
        
        return np.linalg.det(self.data)
        
        

    # TODO: Person 1 & 2 - Implement inverse calculation (inverse)
    # Either code together or have one person code and the other review
    # ...
    def inverse(self):
        """
        calculating the inverse of a matrix
        """
        if(len(self.data) != len(self.data[0])):
            raise ValueError("Matrix must be square")
        
        return np.linalg.inv(self.data)

    # TODO: Person 3 - Implement a function that concatenates two matrices horizontally (hconcat)

    def __hconcat__(self, other):
        """
        Horizontally concatenate this matrix with another
        """
        if len(self.data) != len(other.data):
            raise ValueError("Matrices must have equal number of rows")
        
        return Matrix([self.data[r] + other.data[r] for r in len(self.data)])

    # TODO: Person 3 - Implement a function that concatenates two matrices vertically (vconcat)


    def __vconcat__(self, other):
        """
        Horizontally concatenate this matrix with another
        """
        if len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have equal number of columns")
        
        
        return Matrix(self.data + other.data)

    # TODO: Person 3 & 4 - Implement matrix eigenvalues and eigenvectors (eigen)

    def __eigenvalues__(self, other):
        """
        Horizontally concatenate this matrix with another
        """
        if (len(self.data[0]) != len(other.data[0])) or (len(self.data) != len(other.data)):
            raise ValueError("Matrices must be square")
        
        
        return np.linal.eig(np.array(self.data))

