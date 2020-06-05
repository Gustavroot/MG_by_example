import sys, getopt, os

# Local dir
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/'
# adding examples-related resources
sys.path.append(dir_path + "../base/")
from matrix_factory import Laplace


# Get params from command line
def getCommandParams(argv):

    # Taken from:
    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm

    example_nr = ''
    matrix_type = ''
    try:
        opts, args = getopt.getopt(argv,"he:m:",["example=","matrix="])
    except getopt.GetoptError:
        print('USAGE: test.py -e <example_nr> -m <matrix_type>')
        sys.exit(2)

    if len(opts)==0:
        print('USAGE: test.py -e <example_nr> -m <matrix_type>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('USAGE: main.py -e <example_nr> -m <matrix_type>')
            sys.exit()
        elif opt in ("-e", "--example"):
            example_nr = arg
        elif opt in ("-m", "--matrix"):
            matrix_type = arg

    print('\nExample chosen: '+str(example_nr)+', through the '+str(matrix_type)+' matrix')

    return (int(example_nr), matrix_type)


def createMatrix(matrix_params, matrix_type):

    avail_mat_type = ['laplace']

    if matrix_type not in avail_mat_type:
        raise Exception("The chosen matrix type is not available. Possibilities: "+str(avail_mat_type))

    if matrix_type=="laplace":
        return Laplace(matrix_params)
