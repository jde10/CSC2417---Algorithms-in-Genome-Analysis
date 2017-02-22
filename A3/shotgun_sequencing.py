import numpy as np
import random
a = -1 * np.log(0.0001)
G = 1000000
L = 50
N = int(np.ceil((a*G) / L))
read = []
seq = []
coverage = np.chararray((G,))
coverage[:] = 'K'

# Create a Random Sequence
for i in range(G):
    seq.append(random.choice('ATCG'))
# Create the N starting points
start = np.random.randint(G - (L - 1), size=N)

# Reads
for i in range(N):
    read.append(range(start[i], start[i]+L))


# Coverage
for i in range(len(read)):
    for j in range(L):
        coverage[read[i][j]] = seq[read[i][j]]

# Check uncovered regions:
countN = 0
for i in range(G):
    if coverage[i] is 'K':
        countN += 1

print 'Uncovered Nucleotides:', countN

theory_uncovered = np.exp(-1*(N*L)/G)
uncovered = float(countN)/G
covered = float(G - countN)/G

print ('Percent Uncovered Theory: %.9f' % theory_uncovered)
print ('Percent Uncovered: %.9f' % uncovered)
print ('Percent Covered: %.9f' % covered)
print ('Coverage: %5.f' % a)





