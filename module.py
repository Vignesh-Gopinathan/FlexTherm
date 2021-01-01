# python3 module.py processor0.csv processor1.csv processor2.csv processor3.csv processor4.csv processor5.csv processor6.csv processor7.csv processor8.csv processor9.csv processor10.csv processor11.csv processor12.csv processor13.csv processor14.csv processor15.csv processor16.csv processor17.csv processor18.csv processor19.csv processor20.csv processor21.csv processor22.csv processor23.csv processor24.csv processor25.csv processor26.csv processor27.csv processor28.csv processor29.csv processor30.csv processor31.csv processor32.csv processor33.csv processor34.csv processor35.csv processor36.csv processor37.csv processor38.csv processor39.csv processor40.csv processor41.csv processor42.csv processor43.csv processor44.csv processor45.csv processor46.csv processor47.csv processor48.csv processor49.csv processor50.csv processor51.csv processor52.csv processor53.csv
import sys
import os
import numpy as np
from subprocess import call

i = 1
d = 0
tdata = []
parameter = ["Tl", "Epot", "q", "boundary"]
# tdata[0][1][2] = processor 0 details,second parameter details, end value of second parameter.

while i<len(sys.argv):
    data = (np.genfromtxt(sys.argv[i],delimiter=';'))
    i+=1
    tdata.append(np.abs(data))

root = os.getcwd()
file = root + '/template.sh'
with open(file, 'r') as file:
    filedata = file.read()

for p in range(0,np.size(tdata,0)):
    f_loc = root + '/' + str(p) + '.sh'
    f = open(f_loc,'w+')
    f.write("base=$(pwd)\n")
    for l in range(0,np.size(tdata,1)):
        if (l == 0):
             f.write("for " + parameter[l] + " in $(seq " + str(int(tdata[p][l][d])) + " " + str(int(tdata[p][l][d+1])) + " " + str(int(tdata[p][l][d+2])) + ");do\n")
        else:
            f.write("for " + parameter[l] + " in $(seq " + str(tdata[p][l][d]) + " " + str(tdata[p][l][d+1]) + " " + str(tdata[p][l][d+2]) + ");do\n")
    f.write(filedata)
    for l in range(0,np.size(tdata,1)):
        f.write("done\n")
    f.close()
    with open(f_loc,'r') as file:
        fdata = file.read()
    fdata = fdata.replace('%temp%','temp' + str(p))
    for count in range(0,np.size(tdata,1)):
        fdata = fdata.replace('@'+str(count+1)+'@', parameter[count] + '_${' + parameter[count] + '}')
        fdata = fdata.replace('%'+str(count+1)+'%', '$' + parameter[count])
    with open(f_loc,'w') as file:
        file.write(fdata)
    

