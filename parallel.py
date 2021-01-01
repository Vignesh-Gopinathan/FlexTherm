# mpiexec -n 4 python3 -m mpi4py parallel.py
from mpi4py import MPI
from subprocess import call

comm = MPI.COMM_WORLD
my_rank = comm.rank
call("chmod +x " + str(my_rank)+ ".sh", shell=True)
call("./" + str(my_rank) + ".sh", shell=True)
