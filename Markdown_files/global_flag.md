## Verification tests flag works: 
Needs to be automatic later. 
For now; 

Flag = 1, ranks 4, global aray size (2^3)^3 last number should be; 512

### MPIIO
<div>
<img src="imgs/odMPIIO.png" width="500"/>
</div>

### PHDF5
<div>
<img src="imgs/h5dump_PHDF5_global.png" width="500"/>
</div>

### ADIOS2_HDF5
<div>
<img src="imgs/h5dump_ADIOS2_HDF5.png" width="500"/>
</div>

### ADIOS2_BP4
<div>
<img src="imgs/h5dump_adios2.png" width="500"/>
</div>

## However, ranks 3 create problem. Need to rectify uneven numbers. 
<div>
<img src="imgs/rank3.png" width="500"/>
</div>

