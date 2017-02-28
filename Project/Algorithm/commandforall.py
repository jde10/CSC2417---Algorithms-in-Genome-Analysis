from os import listdir
from os.path import isfile, join


dir = "./results"
onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]


file = open('test.txt', 'w')

for item in onlyfiles:
    line = './qscore -test ../sabre_results/Test/'+item+' -ref ../sabre_results/Ref/'+item[0:7]+' -seqdiffwarn -ignoremissingseqs -ignoretestcase -truncname -quiet >> allresults.txt'
    file.write("%s\n" % line)
