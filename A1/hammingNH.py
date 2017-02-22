
def hammingNH(sequence, kmers):
    distArray = [10.0] * len(kmers)
    minHam = []
    for j in range(0, len(kmers)):
        distArray[j] = hammingDistance(sequence, kmers[j])
        if (distArray[j] <= 1):
            minHam.append(kmers[j])
    return distArray, minHam

def hammingDistance(x, y):
    #from week 4 Alignment slides
    assert len(x) == len(y)
    nmm = 0
    for i in xrange(0, len(x)):
        if x[i] != y[i]:
            nmm +=1
    return nmm