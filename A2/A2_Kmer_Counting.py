from kmerCount import kmerCount
import datetime as t
import itertools
import matplotlib.pyplot as plt
import numpy

# 1.4 k-mer counting

# open data
with open('./q3-reads.fa', 'r') as q3:
        l = 0
        data = []
        for line in q3:
                if l % 2 != 0:
                        data.append(line.strip())
                l += 1

q3.close()

#start timer
to = t.datetime.now()
# k-mers
k = 21
test14 = kmerCount(data, k)
print "Total time:", (t.datetime.now()-to).total_seconds()

unique = sum(1 for x in test14.values() if x==1)

print "Unique 21-mers: %d" % unique

plt.figure(1)
plt.hist(test14.values())
plt.ylabel('Count for k-mer length k=%d' % k)
plt.xlabel('k-mer repeats')
plt.title('Histogram: k-mer=%d' % k)
plt.show()

