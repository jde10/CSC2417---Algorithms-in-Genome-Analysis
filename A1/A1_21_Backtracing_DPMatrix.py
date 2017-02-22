from dpBacktracing import dpBacktracing

# 2.1 Backtracing through dynamic programming matrix

X = 'AGTAGGCATAGAATGATAGTAGACCAGTAGACAGTACTTAGA'
Y = 'AGTAGCATAGAATGATATGTAGACCAGTCGACAGTACTTAGA'

test21, bd_X, bd_A, bd_Y = dpBacktracing(X, Y)

print (''.join(bd_X))
print (''.join(bd_A))
print (''.join(bd_Y))