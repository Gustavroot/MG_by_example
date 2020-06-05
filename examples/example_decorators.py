import time

def example_info(example_nr):
    def info(example):

        avail_examples = [1]

        # check if example is available
        if example_nr not in avail_examples:
             raise Exception(f'The provided example number \
                                is not in our examples bank. \
                                Available examples: {avail_examples}')

        print(f"\nRunning example number {example_nr} ...")

        def wrapper(*arg, **kw):
            result = example(*arg, **kw)
            print("... done\n")
            return result
        return wrapper
    return info


def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        result = func(*arg, **kw)
        t2 = time.time()
        print(f'Time it took {t2 - t1} ms\n')
        return result
    return wrapper