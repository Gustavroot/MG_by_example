import sys, os

# Local dir
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
# adding examples-related resources
sys.path.append(dir_path + "../base/")
from matrix import Matrix
from factory import Jacobi


def EXAMPLE01():

    print("\nUSING JACOBI\n")

    # input params
    matrix_params = []
    solver_params = []

    # create the matrix and solver, based on input params
    matrix = Matrix(matrix_params)
    solver = Jacobi(solver_params, matrix)

    # right hand side
    rhs = []

    # solve
    solver.solve(rhs)
