data = \
    """

    """

import re
import os

# a = re.findall('accuracy:\s+[\d]{1,2}.[\d]{1,10}', data)
# loss = re.findall('loss:\s+[0-9]\.[0-9]+e-[0-9]{1,2}|loss:\s+[0-9]\.[0-9]', data)
#
# ACC = [float(i.split(':')[1]) for i in a]
# Loss = [float(i.split(':')[1]) for i in loss]
#
# PATH = 'JP_J2CP_C'
#
# with open('Classifier\\' + PATH + '\ACC.txt', 'w') as f:
#     f.write(str(ACC))
#
# with open('Classifier\\' + PATH + '\loss.txt', 'w') as f:
#     f.write(str(Loss))

d = re.findall('d_loss:\s+[\d]{1,2}.[\d]{1,2}', data)
g = re.findall('G_loss:\s+[\d]{1,2}.[\d]{1,2}', data)
a2b = re.findall('A2B:\s+[\d]{1,2}.[\d]{1,2}', data)
b2a = re.findall('B2A:\s+[\d]{1,2}.[\d]{1,2}', data)
cl = re.findall(' Cycle_loss:\s+[\d]{1,2}.[\d]{1,2}', data)
dal = re.findall('DA_loss:\s+[\d]{1,2}.[\d]{1,2}', data)
dbl = re.findall('DB_loss:\s+[\d]{1,2}.[\d]{1,2}', data)

A2B = [float(i.split(':')[1]) for i in a2b]
B2A = [float(i.split(':')[1]) for i in b2a]
D = [float(i.split(':')[1]) for i in d]
G = [float(i.split(':')[1]) for i in g]
CL = [float(i.split(':')[1]) for i in cl]
DAL = [float(i.split(':')[1]) for i in dal]
DBL = [float(i.split(':')[1]) for i in dbl]

with open('rock2pop\d_loss.txt', 'w') as f:
    f.write(str(D))

with open('rock2pop\g_loss.txt', 'w') as f:
    f.write(str(G))

with open('rock2pop\\a2b.txt', 'w') as f:
    f.write(str(A2B))

with open('rock2pop\\b2a.txt', 'w') as f:
    f.write(str(B2A))

with open('rock2pop\cl_loss.txt', 'w') as f:
    f.write(str(CL))

with open('rock2pop\da_loss.txt', 'w') as f:
    f.write(str(DAL))

with open('rock2pop\db_loss.txt', 'w') as f:
    f.write(str(DBL))
