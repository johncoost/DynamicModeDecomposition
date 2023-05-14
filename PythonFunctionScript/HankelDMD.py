import numpy as np

def DMD(data, r):
    ## Build data matrices
    X = data[:,:-1]
    X_prime = data[:,1:]
    print(X, X_prime)
    ## Perform singular value decomposition on X1
    u, s, v = np.linalg.svd(X, full_matrices = False)
    print(u, s, v)
    ## Compute the Koopman matrix
    A_tilde = u[:, : r].conj().T @ X_prime @ v[: r, :].conj().T * np.reciprocal(s[: r])
    print(A_tilde)
    ## Perform eigenvalue decomposition on A_tilde
    Phi, Q = np.linalg.eig(A_tilde)
    print(Phi, Q)
    ## Compute the coefficient matrix
    Psi = X_prime @ v[: r, :].conj().T @ np.diag(np.reciprocal(s[: r])) @ Q
    A = Psi @ np.diag(Phi) @ np.linalg.pinv(Psi)
    print(Psi, A)
    
    return A_tilde, Phi, A

def DMDForecast(data, r, pred_step):
    N, T = data.shape
    _, _, A = DMD(data, r)
    mat = np.append(data, np.zeros((N, pred_step)), axis = 1)
    for s in range(pred_step):
        mat[:, T + s] = A @ mat[:, T + s - 1].real
    return mat[:, - pred_step :]
