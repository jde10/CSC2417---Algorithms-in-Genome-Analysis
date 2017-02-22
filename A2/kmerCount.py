from operator import itemgetter
from collections import OrderedDict
from memory_profiler import profile

#@profile
def kmerCount(sequence, k):

    #amount of k lenght kmers in sequence
    N = 1 + len(sequence[0]) - k

    kmers = {}
    for h in range(len(sequence)):
        for i in range(N):
            kmer = sequence[h][i:i+k]

            if kmer in kmers:
                kmers[kmer] +=1
            else:
                kmers[kmer] = 1

    return kmers
