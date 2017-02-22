from Bio import SeqIO
from revComplement import revComplement
from generatekDNA import generatekDNA
from hammingNH import hammingNH
from kmerCount import kmerCount
import itertools
import collections
from dpBacktracing import dpBacktracing
from dpBacktracing import edDistDP
from dpBacktracing import dpBacktracingLast
import datetime as t

'''
# 1.1 Reverse Complementing a DNA sequence
test11 = revComplement('ACTGATGT')

print(test11)

# 1.2 Generating strings from the DNA alphabet
test12 = generatekDNA(5)

print("\n".join(test12))

# 1.3 Hamming Neighbourhood
(dist13, test13) = hammingNH('ACGTA', test12)

print(test13)
'''
# 1.4 k-mer counting

# open data
with open('/Users/JDLVF/Documents/UofT/Fall_2016/CSC2417_AGA/A1/chr20.fa', 'r') as chr20:
        data = chr20.read().replace('\n', '').replace('N', '').replace('\r', '').replace(' ', '')
chr20.close()
data = data.upper()

#start timer
to = t.datetime.now()
# 8-mers
test14 = kmerCount(data, 8)
print "Total time:", (t.datetime.now()-to).total_seconds()

# calculate
# print first 100 items
first100 = itertools.islice(test14.items(), 0, 100)

for key, value in first100:
    print key, value

'''
# 50-mers
test14 = kmerCount(data, 50)
# print first 20 items
first20 = itertools.islice(test14.items(), 0, 20)

for key, value in first20:
    print key, value

'''

# 2.1 Backtracing through dynamic programming matrix
'''
X = 'AGTAGGCATAGAATGATAGTAGACCAGTAGACAGTACTTAGA'
Y = 'AGTAGCATAGAATGATATGTAGACCAGTCGACAGTACTTAGA'

test21, bd_X, bd_A, bd_Y = dpBacktracing(X, Y)

print (''.join(bd_X))
print (''.join(bd_A))
print (''.join(bd_Y))
'''

# 2.2 Counting the number of Optimal Alignments
'''
X_2 = 'AGTAGGCATAGAATGATAGTAAAGACCAGTAGACAGTACTTAGA'
Y_2 = 'AGTAGGCATTAGAATGATAGTAGACCAGTAGACAGTACTTAGA'

print X_2

dpBacktracingLast(X_2, Y_2)

'''