import sys
import os
import math
import functools

LIST_CLASS = ('轻快','婉约','劲爆','节奏感强')

def calc_cos(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
    length = len(v1)
    sxy = 0.0
    sx2 = 0.0
    sy2 = 0.0
    for i in range(length):
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
fname = open('.\\name_No.txt')

dtrain = ftrain.readlines()
dtest = ftest.readlines()
dname = fname.readlines()


ltrain = []
for s in dtrain:
    ltemp = {}
    stemp = s.split()
    length = len(stemp)
    ltemp[0] = stemp[0]
    for i in range(1,length):
        ltemp[i] = stemp[i].split(':')[1]
    ltrain.append(ltemp)

lname = {}
for s in dname:
    stemp = s.split('\t')
    lname[int(stemp[1])] = stemp[0]

len_dtest = len(dtest)
for i in range(len_dtest):
    lclac = []
    stest = {}
    stemp = dtest[i].split()
    length = len(stemp)
    stest[0] = stemp[0]
    for j in range(1,length):
        stest[j] = stemp[j].split(':')[1]
    print("the class of vector%d is %s, which refers to %s" % (i+1,LIST_CLASS[int(stest[0])-1],lname[i+1]))
    for j in range(len(ltrain)):
        if ltrain[j][0] == stest[0]:
            cosine = calc_cos(ltrain[j],stest)
            lclac.append((j,cosine))
    lclac.sort(key=functools.cmp_to_key(compare),reverse=True)
    print("the most 3 similar vectors are %d, %d and %d, and the cosines are %f, %f and %f, which refer to %s, %s and %s" % (lclac[0][0]+1,lclac[1][0]+1,lclac[2][0]+1,lclac[0][1],lclac[1][1],lclac[2][1],lname[lclac[0][0]+1],lname[lclac[1][0]+1],lname[lclac[2][0]+1]))

ftrain.close
ftest.close
fname.close