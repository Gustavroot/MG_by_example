import sys, os
# from examples._examples import EXAMPLE
from examples.example01 import EXAMPLE01
from utils.misc import getCommandParams 

if __name__=='__main__':

    # extraction, from input params, the example to run
    command_params = getCommandParams(sys.argv[1:])
    example_nr = command_params[0]
    matrix_type = command_params[1]

    # run the chosen example
  
    EXAMPLE01(matrix_type)
