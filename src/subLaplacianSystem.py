import numpy as np


def is_sublaplacian_system(A):
    # Check if A is square
    if A.shape[0] != A.shape[1]:
        return False

    # Check if A is symmetric and positive definite
    if not np.allclose(A, A.T) or np.any(np.linalg.eigvals(A) <= 0):
        print("Not positive definite or not symm")
        return False

    # Check if diagonal entries are positive
    if np.any(np.diag(A) <= 0):
        print("Not all diagonal entries are +ve")
        return False

    # Check if off-diagonal entries are non-positive
    if np.any(A - np.diag(np.diag(A)) > 0):
        print("Not all off diagonal entries are non -+ve")
        return False

    # Check if row sums are non-positive
    if np.any(np.sum(A, axis=1) > 0):
        print("Not all rows sums are non-positive")
        return False

    # If all conditions are satisfied, A is a sub-Laplacian system
    return True


if __name__ == "__main__":
    A = np.array([[3, -1, -1, -1], [-1, 2, -1, 0], [-1, -1, 2, 0], [-1, 0, 0, -1]])
    B = np.array([[2, -1, 0, -1], [-1, 3, -1, 0], [0, -1, 2, -1], [-1, 0, -1, 1]])
    C = np.array([[3, -1, -1], [-1, 2, 0], [-1, 0, 2]])
    print(is_sublaplacian_system(C))
