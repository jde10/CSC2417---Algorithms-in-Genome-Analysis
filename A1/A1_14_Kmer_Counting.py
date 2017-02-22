from kmerCount import kmerCount
import datetime as t
import itertools

# 1.4 k-mer counting

# open data
with open('./chr20.fa', 'r') as chr20:
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
first100 = itertools.islice(test14.items(), 0, 100)

for key, value in first100:
    print key, value

'''