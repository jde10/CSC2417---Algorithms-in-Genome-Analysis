import numpy as np
import matplotlib.pyplot as plt
# G genome length
# L read length in nucleotides
# N number of reads sequenced
# a NL/G

G = 3000000000
L = [100, 1000, 10000]
a = np.arange(0, 10, 0.001)

contigs = [[],[],[]]

for j in range(len(L)):
    for i in range(len(a)):
        contigs[j].append(((a[i]*G)/(L[j]))*np.exp(-1*a[i]))

print contigs

plt.figure(1)
plt.plot(a, contigs[0])
plt.plot(a, contigs[1])
plt.plot(a, contigs[2])
plt.legend(['L = 100', 'L = 1000', 'L = 10000'], loc='upper right')
plt.xlabel('Coverage')
plt.ylabel('Expected number of contigs')
plt.title('1.d. Expected number of contigs as a function of Coverage')
plt.show()
plt.savefig('1d_expected_contigs')
