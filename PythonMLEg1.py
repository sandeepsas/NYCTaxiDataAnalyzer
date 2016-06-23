author__ = 'Sandeep_Sasidharan'


from urllib.request import urlopen

import sys

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urlopen(target_url)
#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
 #split on comma

 row = str(line).strip().split(",")
 xList.append(row)
sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))
