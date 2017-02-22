from operator import itemgetter
from collections import OrderedDict
from memory_profiler import profile

#@profile
def kmerCount(sequence, k):

    #amount of k lenght kmers in sequence
    N = 1 + len(sequence) - k

    kmers = {}

    for i in range(N):
        kmer = sequence[i:i+k]

        if kmer in kmers:
            kmers[kmer] +=1
        else:
            kmers[kmer] = 1

    sorted_kmers = OrderedDict(sorted(kmers.items(), key=itemgetter(1), reverse = True))

    return sorted_kmers
