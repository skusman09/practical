#eigen values and eigen vectors
import numpy as np
matrix = np.array([[1,2,3],
[0,-2,6],
[0,0,-3]])
eigenvalues,eigenvectors = np.linalg.eig(matrix)
print(matrix)
print("___Eigen Values:___")
print(eigenvalues)
print("___Eigen Vectors:___")
print(eigenvectors)

rank = np.linalg.matrix_rank(Vector_matrix)
if rank==Vector_matrix.shape[0]:
    print("vectors are linearly independent")
else:
    print("vectors are linearly dependent")

#matrix transpose
import numpy as np
mat = np.array([[1,2,3],[4,5,6]])
t_mat = np.transpose(mat)
print("___original matrix:___")
print(mat)
print("___Transpose of matrix:___")
print(t_mat)

#Diagonal matrix
import numpy as np
mat2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
d_mat = np.diag(mat2)
print("___matrix:___")
print(mat2)
print("___diagonal of matrix:___")
print(d_mat)

#triangular matrix
#Diagonal matrix
import numpy as np
mat3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
upper_tri_mat = np.triu(mat3)
lower_tri_mat = np.tril(mat3)
print("___upper triangular matrix:___")
print(upper_tri_mat)
print("___lower triangular matrix:___")
print(lower_tri_mat)

#orthogonal matrix
import numpy as np
matrix = np.array([[1,0],[0,-1]])
#perform QR decomposition
q,r = np.linalg.qr(matrix)
#check if q is an orthogonal matrix
is_orthogonal = np.allclose(np.dot(q,q.T), np.eye(matrix.shape[0]))
print("___original matrix:___")
print(matrix)
print("___orthogonal matrix (Q from QR decomposition):___")
print(q)
print("___is Q orthogonal?___")
print(is_orthogonal)

