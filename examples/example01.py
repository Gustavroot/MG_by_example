import sys, os
from base.matrix import Matrix
from base.solvers_factory import Jacobi
from utils.misc import createMatrix
from examples.example_decorators import example_info
from examples.example_decorators import timing

@example_info(1)
@timing
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
