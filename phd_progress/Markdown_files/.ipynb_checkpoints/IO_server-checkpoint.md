# Implementation of IO server 

IO server link: 

https://www.cscs.ch/fileadmin/user_upload/contents_publications/tutorials/fast_parallel_IO/SimpleAsyncIOServer_MC.pdf

### mpich 

```
mpicc.mpich -show
gcc -Wl,-Bsymbolic-functions -Wl,-z,relro -I/usr/include/x86_64-linux-gnu/mpich -L/usr/lib/x86_64-linux-gnu -lmpich
```

```
(base) shrey@shrey-HP-EliteDesk-800-G3-SFF:~/Coding/test$ mpicc.mpich  mpi_split_comm.c  && mpirun -n 3 ./a.out 
My rank is 0, color is 0 
My rank is 0, color is 0 
My rank is 0, color is 0
``` 

Error for intercom create: 

```
        MPI_Intercomm_create(ioServeComm, 0,
                         splitComm, 0, myrank3, &interComm);  
```

```
Fatal error in PMPI_Intercomm_create: Invalid rank, error stack:
PMPI_Intercomm_create(336): MPI_Intercomm_create(comm=0x84000002, local_leader=0, comm=0x84000001, remote_leader=0, tag=0, newintercomm=0x7ffef2d982b0) failed
PMPI_Intercomm_create(306): Local and remote leaders must be different processes
[unset]: write_line error; fd=-1 buf=:cmd=abort exitcode=873049350
:
```



### openmpi 
```
mpicc --showme 
gcc -I/usr/lib/x86_64-linux-gnu/openmpi/include/openmpi -I/usr/lib/x86_64-linux-gnu/openmpi/include -pthread -L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi
```

```
(base) shrey@shrey-HP-EliteDesk-800-G3-SFF:~/Coding/test$ mpicc mpi_split_comm.c  && mpirun -n 3 ./a.out 
My rank is 0, color is 0 
My rank is 0, color is 1 
My rank is 1, color is 1 

```
