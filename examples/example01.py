import sys, os

# Local dir
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
# adding examples-related resources
sys.path.append(dir_path + "../base/")
from matrix import Matrix
#from matrix import create
from solvers_factory import Jacobi
# adding examples-related resources
sys.path.append(dir_path + "../utils/")
from misc import createMatrix


def EXAMPLE01(matrix_type):

    print("\nUSING JACOBI\n")

    # input params
    matrix_params = dict()
    solver_params = dict()

    # create the matrix and solver, based on input params
    matrix = createMatrix(matrix_params, matrix_type)
    solver = Jacobi(solver_params, matrix)

    # right hand side
    rhs = []

    # solve
    solver.solve(rhs)
