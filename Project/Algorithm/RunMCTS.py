from Bio import SeqIO
import numpy as np
from multi_NMCTS import NMonteCarlo

# All file names with # of sequences
file_names = open("./bali2dna/info/nseqs.txt")
file = []
seq_n = []
for lines in (raw.strip().split(';') for raw in file_names):
    file.append(lines[0])
    seq_n.append(lines[1])

print file[0], seq_n[0]

size = []



#open file
dir = "./bali2dna/in/"

for i in range(len(file)):
    # Variables for opening the file

    sequence = []
    id = []

    for record in SeqIO.parse(dir+file[i], "fasta"):
        sequence.append(str(record.seq))
        id.append(record.id)

    print len(sequence)
    if len(sequence) == 3:
        # Variables for time management
        pair_time = np.ceil(40*60)
        total_time = pair_time * 9

        NMonteCarlo(sequence, id, file[i], pair_time, total_time, 1)

# sequence = []
# id = []
#
# for record in SeqIO.parse(dir + "1tvxA_ref1", "fasta"):
#     sequence.append(str(record.seq))
#     id.append(record.id)
#
# print len(sequence[0])
# size.append(len(sequence[0]))
# # Variables for time management
# pair_time = np.ceil(60*60)
# total_time = 360*60
#
# NMonteCarlo(sequence, id, "1tvxA_ref1", pair_time, total_time, 1)
