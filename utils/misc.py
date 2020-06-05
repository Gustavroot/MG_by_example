import sys, getopt

# Get params from command line
def getCommandParams(argv):

    # Taken from:
    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm

    example_nr = ''
    try:
        opts, args = getopt.getopt(argv,"he:",["example="])
    except getopt.GetoptError:
        print('USAGE: test.py -e <example_nr>')
        sys.exit(2)

    if len(opts)==0:
        print('USAGE: test.py -e <example_nr>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('USAGE: main.py -e <example_nr>')
            sys.exit()
        elif opt in ("-e", "--example"):
            example_nr = arg
    print('\nExample chosen: '+str(example_nr))

    return int(example_nr)
