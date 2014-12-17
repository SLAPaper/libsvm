import sys
import os
import math
import functools

def calc_cos(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
    length = len(v1)
    sxy = 0.0
    sx2 = 0.0
    sy2 = 0.0
    for i in range(length - 1):
        sxy += float(v1[i]) * float(v2[i])
        sx2 += float(v1[i]) * float(v1[i])
        sy2 += float(v2[i]) * float(v2[i])
    result = sxy / math.sqrt(sx2 * sy2)
    return result

def compare(kw_only1, kw_only2):
    return kw_only1[1] - kw_only2[1]

if len(sys.argv) <= 2:
    print('usage: {0} training_file testing_file'.format(sys.argv[0]))
    raise systemexit

train_filename = sys.argv[1]
assert os.path.exists(train_filename),'trianing file not found'

test_filename = sys.argv[2]
assert os.path.exists(test_filename),'testing file not found'

ftrain = open(train_filename)
ftest = open(test_filename)

dtrain = ftrain.readlines()
dtest = ftest.readlines()

ltrain = []
for s in dtrain:
    ltemp = {}
    stemp = s.split()
    length = len(stemp)
    ltemp[0] = stemp[0]
    for i in range(1,length - 1):
        ltemp[i] = stemp[i].split(':')[1]
    ltrain.append(ltemp)

lclac = []
for s in dtest:
    stest = {}
    stemp = s.split()
    length = len(stemp)
    stest[0] = stemp[0]
    for i in range(1,length - 1):
        stest[i] = stemp[i].split(':')[1]
    for i in range(len(ltrain) - 1):
        if ltrain[i][0] == stest[0]:
            cosine = calc_cos(ltrain[i],stest)
            lclac.append((i,cosine))

#max = (0,0)
#for s in lclac:
#    if s[1] > max[1]:
#        max = s
lclac.sort(key=functools.cmp_to_key(compare),reverse=True)
print("the most 3 similar vectors are %d, %d and %d, and the cosines are %f, %f and %f" % (lclac[0][0]+1,lclac[1][0]+1,lclac[2][0]+1,lclac[0][1],lclac[1][1],lclac[2][1]))

ftrain.close
ftest.close