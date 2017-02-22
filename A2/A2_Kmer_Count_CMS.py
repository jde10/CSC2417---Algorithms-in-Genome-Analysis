from countminsketch import CountMinSketch
import matplotlib.pyplot as plt
# 3.b

# open data
with open('./q3-reads.fa', 'r') as q3:
        l = 0
        seq = []
        for line in q3:
            if l % 2 != 0:
                seq.append(line.strip())
            l+=1

q3.close()
k = 21
m = [10000, 50000, 100000, 500000, 1000000]



for j in range(len(m)):
    N = 1 + len(seq[j]) - k
    sketch = CountMinSketch(m[j], 5)  # m=1000, d=10
    for h in range(len(seq)):
        for i in range(0, N):
            sketch.add(seq[h][i:i + k])

    count = 0
    for h in range(len(seq)):
        for i in range(0, N):
            if sketch[seq[h][i:i + k]] == 1:
                count +=1


    print 'For m = %d \n Estimate for k-mers = %d' % (m[j], count)
