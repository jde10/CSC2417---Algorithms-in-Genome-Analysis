import itertools

def generatekDNA (k):

    alphabet = ['A', 'T', 'C', 'G']

    keywords = [''.join(i) for i in itertools.product(alphabet, repeat = k)]

    kmers = sorted(keywords)

    return kmers