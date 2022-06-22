## A64FX



Default modules 



```
Currently Loaded Modulefiles:
 1) cpe-cray                  3) craype/2.7.0(default)   5) craype-network-infiniband        7) gcc/10.2.0                                   9) cmake/3.20.1  
 2) cce-sve/10.0.1(default)   4) craype-arm-nsp1         6) cray-libsci/20.09.1.1(default)   8) cray-mvapich2_noslurm_nogpu/2.3.4(default)  
``` 

### ADIOS2 linked with HDF5

This works well. The shared library command is switched off and the HDF5 is not linked. One concern is that cxx compiler is cray/10.1 but the gcc compiler is gnu/8.01

```
cmake -DMPIEXEC_EXECUTABLE=/opt/cray/pe/cray-mvapich2_noslurm_nogpu/2.3.4/infiniband/cray/10.0/bin/mpiexec -DCMAKE_C_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gcc -DCMAKE_Fortran_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gfortran -DADIOS2_USE_Fortran=OFF -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=$ADIOS2_DIR -DADIOS2_USE_HDF5=OFF ../ADIOS2/
```

### ADIOS2 shared libraries 
```
cmake -DMPIEXEC_EXECUTABLE=/opt/cray/pe/cray-mvapich2_noslurm_nogpu/2.3.4/infiniband/cray/10.0/bin/mpiexec -DCMAKE_C_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gcc -DCMAKE_Fortran_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gfortran -DADIOS2_USE_Fortran=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=$ADIOS2_DIR -DADIOS2_USE_HDF5=OFF ../ADIOS2/
```
Error:/home/ri-sbhardwaj/adios2-build/lib64/libadios2_core.so.2: undefined reference to `std::runtime_error::runtime_error(std::runtime_error&&)@GLIBCXX_3.4.26'

### ADIOS2 building with HDF5

This doesnt work.  

#### Building HDF5
```
CC=mpicc ./configure --enable-parallel --prefix=$HDF5_DIR
make -j 16
make install 
``` 
```
cmake -DMPIEXEC_EXECUTABLE=/opt/cray/pe/cray-mvapich2_noslurm_nogpu/2.3.4/infiniband/cray/10.0/bin/mpiexec -DCMAKE_C_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gcc -DCMAKE_Fortran_COMPILER=/lustre/projects/bristol/modules-a64fx/gcc/10.2.0/bin/gfortran -DADIOS2_USE_Fortran=OFF -DHDF5_ROOT=$HDF5_DIR -DCMAKE_INSTALL_PREFIX=$ADIOS2_DIR ../ADIOS2/

```


```
/opt/cray/pe/cce-sve/10.0.1/binutils/aarch64/aarch64-unknown-linux-gnu/bin/ld: /home/ri-sbhardwaj/adios2-build/lib64/libadios2_core.so.2: undefined reference to `std::__cxx11::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >::basic_stringstream()@GLIBCXX_3.4.26'
/opt/cray/pe/cce-sve/10.0.1/binutils/aarch64/aarch64-unknown-linux-gnu/bin/ld: /home/ri-sbhardwaj/adios2-build/lib64/libadios2_core.so.2: undefined reference to `std::logic_error::logic_error(std::logic_error&&)@GLIBCXX_3.4.26'
/opt/cray/pe/cce-sve/10.0.1/binutils/aarch64/aarch64-unknown-linux-gnu/bin/ld: /home/ri-sbhardwaj/adios2-build/lib64/libadios2_core.so.2: undefined reference to `std::__cxx11::basic_ostringstream<char, std::char_traits<char>, std::allocator<char> >::basic_ostringstream()@GLIBCXX_3.4.26'
/opt/cray/pe/cce-sve/10.0.1/binutils/aarch64/aarch64-unknown-linux-gnu/bin/ld: /home/ri-sbhardwaj/adios2-build/lib64/libadios2_core.so.2: undefined reference to `std::runtime_error::runtime_error(std::runtime_error&&)@GLIBCXX_3.4.26'
collect2: error: ld returned 1 exit status
make[2]: *** [examples/hello/bpWriter/CMakeFiles/hello_bpWriter_c.dir/build.make:98: bin/hello_bpWriter_c] Error 1
make[1]: *** [CMakeFiles/Makefile2:4188: examples/hello/bpWriter/CMakeFiles/hello_bpWriter_c.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```


## XCI
```
ri-sbhardwaj@xcil00:~> lscpu
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              256
On-line CPU(s) list: 0-255
Thread(s) per core:  4
Core(s) per socket:  32
Socket(s):           2
NUMA node(s):        2
Vendor ID:           Cavium
Model:               2
Model name:          ThunderX2 99xx
Stepping:            0x1
BogoMIPS:            400.00
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            32768K
NUMA node0 CPU(s):   0-31,64-95,128-159,192-223
NUMA node1 CPU(s):   32-63,96-127,160-191,224-255
Flags:               fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics cpuid asimdrdm
``` 

CPUs are 256, but are overthreaded. If threading is not needed, then only 64 MPI ranks per node. Node has 2 sockets, with 32 cores. 

https://gw4-isambard.github.io/docs/user-guide/XCI.html

Built environment, use qsub for pbs script. 

```qsub isambard_xci.pbs``` 

```/home/ri-sbhardwaj/benchmark_c/Source_files/bench: error while loading shared libraries: libzmq.so.5: cannot open shared object file: No such file or directory``` 

Shut off zeromq in adios2 build 

```cmake -DCMAKE_INSTALL_PREFIX=$ADIOS2_DIR -DHDF5_ROOT=$HDF5_DIR -DADIOS2_USE_ZeroMQ=OFF ../ADIOS2``` 

<div>
<img src="imgs/adios2_xcl.png" width="500"/>
</div>

Still problems with zeromq

Install libzmq 
```
git clone https://github.com/zeromq/libzmq.git
./autogen.sh 
./configure CC=cc --prefix=$LIBZMQ_DIR
make 
make install 
export LD_LIBRARY_PATH=$LIBZMQ_DIR/lib:$LD_LIBRARY_PATH
``` 


## PBS script issues 
http://docs.adaptivecomputing.com/torque/6-1-2/adminGuide/torque.htm#topics/torque/2-jobs/requestingOtherRes.htm%3FTocPath%3DChapter%25203%253A%2520Submitting%2520and%2520Managing%2520Jobs%7C3.1%2520%25C2%25A0Job%2520Submission%7C_____7
