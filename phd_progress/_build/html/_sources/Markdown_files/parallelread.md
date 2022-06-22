Code taken from PETSc from Paul to read the correct hyperslabs from the dataset even if the size is not divisible by dataset total global dimensions. 

https://petsc.org/release/src/ksp/ksp/tutorials/ex3.c.html

```
    start[0] = rank*(DIM1/size) + ((DIM1%size) < rank ? (DIM1%size) : rank);
    start[1] = 0;

    end[0]   = start[0] + DIM1/size + ((DIM1%size) > rank);
    end[1]   = DIM2;

    count[0] = end[0] - start[0];
    count[1] = end[1] - start[1];
``` 

<div>
<img src="imgs/h5dump_comparison.png" width="500"/>
</div>

A comparision between h5dump of a test hdf5 file and the file first read and then written out by program. Conducted across 2 and 3 ranks. 
This confirms that all ranks are reading their respective slabs. 