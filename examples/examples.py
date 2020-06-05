from example01 import EXAMPLE01


def EXAMPLE(example_nr):

    avail_examples = [1]

    # check if example is available
    if example_nr not in avail_examples:
         raise Exception("The provided example number is not in our examples bank. Available examples: "+str(avail_examples))

    print("\nRunning example number "+str(example_nr)+"...")

    if example_nr==1:
        EXAMPLE01()

    print("... done\n")
