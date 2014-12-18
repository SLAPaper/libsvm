import sys
import os
import math
import functools

LIST_CLASS = ('未知','轻快','抒情','劲爆','节奏感强')

def calc_cos(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
        raise SystemExit
    length = len(v1)
    sxy = 0.0
    sx2 = 0.0
    sy2 = 0.0
    for i in range(1,length):
        sxy += float(v1[i]) * float(v2[i])
        sx2 += float(v1[i]) * float(v1[i])
        sy2 += float(v2[i]) * float(v2[i])
    if sx2 * sy2 == 0:
        return 0
    else:
        result = sxy / math.sqrt(sx2 * sy2)
        return result

def calc_dis(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
        raise SystemExit
    length = len(v1)
    result2 = 0.0
    for i in range(1,length):
        result2 += (float(v1[i]) - float(v2[i])) ** 2
    return result2

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

lname = []
for s in dname:
    stemp = s.split('\t')
    lname.append(stemp[0])

len_dtest = len(dtest)
for i in range(len_dtest):
    lcalc = []
    lcalc_dis = []
    stest = {}
    stemp = dtest[i].split()
    length = len(stemp)
    stest[0] = stemp[0]
    for j in range(1,length):
        stest[j] = stemp[j].split(':')[1]
    print("the class of vector%d is %s" % (i + 1,LIST_CLASS[int(stest[0])]))

    for j in range(len(ltrain)):
        if stest[0] == '0':
            cosine = calc_cos(ltrain[j],stest)
            lcalc.append((j,cosine))
            distance = calc_dis(ltrain[j],stest)
            lcalc_dis.append((j,distance))
        elif ltrain[j][0] == stest[0]:
            cosine = calc_cos(ltrain[j],stest)
            lcalc.append((j,cosine))
            distance = calc_dis(ltrain[j],stest)
            lcalc_dis.append((j,distance))
    lcalc.sort(key=functools.cmp_to_key(compare),reverse=True)
    lcalc_dis.sort(key=functools.cmp_to_key(compare))
    print("the most 3 similar vectors based on cosine are \n\t%d, %d and %d, \n\tand the cosines are %f, %f and %f, \n\twhich refer to %s, %s and %s" % (lcalc[0][0] + 1,lcalc[1][0] + 1,lcalc[2][0] + 1,lcalc[0][1],lcalc[1][1],lcalc[2][1],lname[lcalc[0][0]],lname[lcalc[1][0]],lname[lcalc[2][0]]))
    print("the most 3 similar vectors based on distance are \n\t%d, %d and %d, \n\tand the distances are %f, %f and %f, \n\twhich refer to %s, %s and %s" % (lcalc_dis[0][0] + 1,lcalc_dis[1][0] + 1,lcalc_dis[2][0] + 1,lcalc_dis[0][1],lcalc_dis[1][1],lcalc_dis[2][1],lname[lcalc_dis[0][0]],lname[lcalc_dis[1][0]],lname[lcalc_dis[2][0]]),end='\n\n')

ftrain.close
ftest.close
fname.close