import sys, os

# Local dir
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
# adding examples-related resources
sys.path.append(dir_path + "./examples/")
from examples import EXAMPLE
# adding utils-related resources
sys.path.append(dir_path + "./utils/")
from misc import getCommandParams


if __name__=='__main__':

    # extraction, from input params, the example to run
    command_params = getCommandParams(sys.argv[1:])
    if len(command_params) != 2:
        raise Exception("USAGE: python main.py -e <example_nr> -m <matrix_type>")
    example_nr = command_params[0]
    matrix_type = command_params[1]

    # run the chosen example
    EXAMPLE(example_nr, matrix_type)
