import numpy as np
def validate_matrices(op: str, *matrices: np.ndarray):
    if op == "add" or op == "subtract":
        if not all(m.shape == matrices[0].shape for m in matrices):
            raise ValueError("musza miec takie same wymiary")
    elif op == "multiply":
        if not all(matrices[i].shape[1] == matrices[i+1].shape[0] for i in range(len(matrices)-1)):
            raise ValueError("oba musza miec tyle samo kolumn")
    elif op == "transpose":
        pass
    else:
        raise ValueError("niema " + op)

def perform_matrix_operation(operation: str, *matrices: np.ndarray):
    validate_matrices(operation, *matrices)

    if operation == "add":
        return sum(matrices)
    elif operation == "subtract":
        return matrices[0] - sum(matrices[1:])
    elif operation == "multiply":
        result = matrices[0]
        for m in matrices[1:]:
            result = np.dot(result, m)
        return result
    elif operation == "transpose":
        return [m.T for m in matrices]
    else:
        raise ValueError("niema" + operation)

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("dodawanie", perform_matrix_operation("add", matrix1, matrix2))
print("mnozenie", perform_matrix_operation("multiply", matrix1, matrix2))
print("transpozycja", perform_matrix_operation("transpose", matrix1, matrix2))
