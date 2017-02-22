from hammingNH import hammingNH
from generatekDNA import generatekDNA

# 1.2 Generating strings from the DNA alphabet
test12 = generatekDNA(5)

# 1.3 Hamming Neighbourhood
(dist13, test13) = hammingNH('ACGTA', test12)

print(test13)