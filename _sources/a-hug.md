## A64fx on isambard 
### building environments
https://gw4-isambard.github.io/docs/user-guide/A64FX.html

```module use /lustre/projects/bristol/modules-a64fx/modulefiles```
for upto date cmake modules. 

cray-hdf5 is loaded by default but can change to another version. 
```
hdf5-parallel/1.10.7/arm-21.0-openmpi-4.1.0
hdf5-parallel/1.10.7/cce-sve-10.0-mvapich2  
hdf5-parallel/1.10.7/gcc-11-openmpi-4.1.0  
hdf5/1.12.0/gcc-11  
``` 

mpi module is ```cray-mvapich2_noslurm_nogpu``` 

<div>
<img src="imgs/modulelist_isambard.png" width="1000"/>
</div>

### building adios2 

<div>
<img src="imgs/error_adios2.png" width="1000"/>
</div>
