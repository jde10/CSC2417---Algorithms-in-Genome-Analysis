from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
from os import listdir
from os.path import isfile, join

import numpy as np
import itertools

data = np.load('align_sup_030.npz')
print data.files

alignment = data['alignment']
print alignment.shape

print alignment[0]

id_order = data['id_order']

print id_order

order = data['order']
print order

# for i in range(len(alignment[0])):
#     for j in range (len(alignment[1])):
#         a= ''.join(alignment[i,j])
#
#         a=a.replace("-", ".")
#         print a
dir = "./SabreResults"
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]


for n in range(len(onlyfiles)):
    long_name = onlyfiles[n]
    name = long_name[6:13]

    data = np.load(dir+"/"+long_name)
    alignment = data['alignment']
    id_order = data['id_order']
    order = data['order']

    for i in range(alignment.shape[0]): # number of alignments made
        rec = []
        for j in range(alignment.shape[1]): # number of sequences
            for k in range(alignment.shape[1]): # number of sequences again
                if order[i, k] == j:
                    s = ''.join(alignment[i,k])
                    s = s.replace("-", ".")

                    s_rec = SeqRecord(Seq(s, generic_protein), id=id_order[i,k], description="")
                    rec.append(s_rec)

        SeqIO.write(rec, name+"_"+str(i), "fasta")
