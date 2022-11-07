import numpy as np


def f(x):  # Define the objective function
    return x[0]**2/2 + x[0]*x[1] + x[1]**2 - 2*x[1]


A = np.array(([1/2, 1/2], [1/2, 1]), dtype=float)
b = np.array([0., 2.])


eigs = np.linalg.eigvals(A)
print("The eigenvalues of A:", eigs)

if (np.all(eigs>0)):
    print("A is positive definite")
elif (np.all(eigs>=0)):
    print("A is positive semi-definite")
else:
    print("A is negative definite")


if (A.T==A).all()==True: print("A is symmetric")


def linear_CG(x, A, b, epsilon):
    res = A.dot(x) - b  # Initialize the residual
    delta = -res  # Initialize the descent direction

    while True:

        if np.linalg.norm(res) <= epsilon:
            return x, f(x)  # Return the minimizer x* and the function value f(x*)

        D = A.dot(delta)
        beta = -(res.dot(delta)) / (delta.dot(D))  # Line (11) in the algorithm
        x = x + beta * delta  # Generate the new iterate

        res = A.dot(x) - b  # generate the new residual
        chi = res.dot(D) / (delta.dot(D))  # Line (14) in the algorithm
        delta = chi * delta - res  # Generate the new descent direction


linear_CG(np.array([2.3, -2.2]), A, b, 10**-5)
