import numpy
from copy import deepcopy

def dpBacktracing (x, y):

    D = edDistDP(x, y)
    first = numpy.unravel_index(D[len(x), :].argmin(), D.shape)
    align = []
    bars_dashes_X = []
    bars_dashes_A = []
    bars_dashes_Y = []
    if first[1] != 0:

        xEx = first[1] - 1
        yEx = len(D) - 2

        bars_dashes_X.insert(0, x[yEx])
        bars_dashes_A.insert(0, '|')
        bars_dashes_Y.insert(0, y[xEx])

        #print D[yEx, xEx]

        while (yEx > 0) and (xEx > 0):

            if (D[yEx-1, xEx] < D[yEx-1, xEx-1]) and (D[yEx-1, xEx] < D[yEx, xEx-1]):
                yEx -= 1
                align.insert(0, 'D')
                bars_dashes_X.insert(0, x[yEx])
                bars_dashes_A.insert(0, ' ')
                bars_dashes_Y.insert(0, '-')

            elif (D[yEx - 1, xEx - 1] <= D[yEx - 1, xEx]) and (D[yEx - 1, xEx - 1] <= D[yEx, xEx - 1]):
                yEx -= 1
                xEx -= 1
                align.insert(0, 'M')
                bars_dashes_X.insert(0, x[yEx])
                bars_dashes_A.insert(0, '|')
                bars_dashes_Y.insert(0, y[xEx])

            elif (D[yEx, xEx - 1] < D[yEx - 1, xEx - 1]) and (D[yEx, xEx - 1] < D[yEx - 1, xEx]):
                xEx -= 1
                align.insert(0, 'I')
                bars_dashes_X.insert(0, '-')
                bars_dashes_A.insert(0, ' ')
                bars_dashes_Y.insert(0, y[xEx])

    return align, bars_dashes_X, bars_dashes_A, bars_dashes_Y

def dpBacktracingLast (x, y):

    D = edDistDP(x, y)
    first = numpy.unravel_index(D[len(x), :].argmin(), D.shape)
    bars_dashes_X = ""
    bars_dashes_A = ""
    bars_dashes_Y = ""

    #xEx = first[1] - 1
    #yEx = len(D) - 2
    xEx = len(y)
    yEx = len(x)

    rBacktracing(D, x, y, xEx, yEx, bars_dashes_X, bars_dashes_A, bars_dashes_Y)


    return bars_dashes_X, bars_dashes_A, bars_dashes_Y

def rBacktracing (D, x, y, xEx, yEx, bars_dashes_X, bars_dashes_A, bars_dashes_Y):

    if xEx == 0 and yEx == 0:
        print('\n-----------------Alignment------------------ \n')
        print (''.join(bars_dashes_X))
        print (''.join(bars_dashes_A))
        print (''.join(bars_dashes_Y))
        print('\n')

        return

    if (D[yEx, xEx - 1] + 1) == D[yEx, xEx]:

        rBacktracing(D, x, y, xEx - 1, yEx, "-" + bars_dashes_X, " "+bars_dashes_A, y[xEx - 1] + bars_dashes_Y)

    if (D[yEx - 1, xEx] + 1) == D[yEx, xEx]:

        rBacktracing(D, x, y, xEx, yEx - 1, x[yEx - 1] + bars_dashes_X, " " + bars_dashes_A, "-" + bars_dashes_Y)

    delt = 1 if x[yEx - 1] != y[xEx - 1] else 0

    if D[yEx - 1, xEx - 1]  == D[yEx, xEx] + delt:

        rBacktracing(D, x, y, xEx - 1, yEx - 1, x[yEx - 1] + bars_dashes_X, "|" + bars_dashes_A, y[xEx - 1] + bars_dashes_Y)



def edDistDP (x, y):

    """ Calculate edit distance between sequences x and y using
            matrix dynamic programming.  Return distance. """
    D = numpy.zeros((len(x) + 1, len(y) + 1), dtype=int)
    D[0, 1:] = range(1, len(y) + 1)
    D[1:, 0] = range(1, len(x) + 1)
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            delt = 1 if x[i - 1] != y[j - 1] else 0
            D[i, j] = min(D[i - 1, j - 1] + delt, D[i - 1, j] + 1, D[i, j - 1] + 1)
    return D