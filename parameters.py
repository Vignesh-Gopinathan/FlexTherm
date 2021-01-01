import numpy as np
import sys

Tl = np.arange(1200,1245,5)
Epot = np.arange(0.0247,0.03455,0.001647)
q = np.arange(5000,27500,2500)
boundary = np.arange(0.955,1.005,0.01)
j = 0
k = 0

for i in range(0,54):
    file = 'processor' + str(i) + '.csv'
    f_loc = '/home/poolhiwi/Vignesh/03_Cases/09_ParametricStudy_64processor/Togive/' + file
    f = open(f_loc,'w+')        
    f.write(str(Tl[j]) + ";1;" + str(Tl[j]) + "\n")
    f.write(str(Epot[k]) + ";1;" + str(Epot[k]) + "\n")
    f.write(str(q[0]) + ";2500;" + str(q[-1]) + "\n")
    f.write(str(boundary[0]) + ";0.01;" + str(boundary[-1]) + "\n")
    k += 1
    if (k == 6):
        j += 1
        k = 0
    f.close()
        
        
