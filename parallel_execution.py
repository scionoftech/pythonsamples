import time
from joblib import Parallel, delayed
import multiprocessing

'''' Sample 1'''


# A function that can be called to do work:
def work(arg):
    print("Function receives the arguments as a list:", arg)
    # Split the list to individual variables:
    i, j = arg
    # All this work function does is wait 1 second...
    time.sleep(1)
    # ... and prints a string containing the inputs:
    print("%s_%s" % (i, j))
    return ("%s_%s" % (i, j))


def start():
    # List of arguments to pass to work():
    arg_instances = [(1, 1), (1, 2), (1, 3), (1, 4)]
    # Anything returned by work() can be stored:
    results = Parallel(n_jobs=4, verbose=1, backend="threading")(map(delayed(work), arg_instances))
    print(results)


''''Sample 2'''


def processInput(i):
    time.sleep(10 - i)
    print(i)
    # return i * j


def srt():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_cores = multiprocessing.cpu_count()
    print(num_cores)
    i = 0
    for x in range(0, 10, 4):
        zz = a[x:x + 4]
        i += 1
        print('loop', i)
        Parallel(n_jobs=num_cores, prefer="threads")(delayed(processInput)(i) for i in zz)
        # print(results)


if __name__ == '__main__':
    srt()
