## Read input file from crescendo, had to malloc specify the dimensions and size for the job submission to work.
Each rank writes the whole data set locally. 

## TO DO: 
- Global write CRESCENDO
- Read and write CRESCENDO in parallel 
- Calculate volume of the mesh, using topology mesh  
- In functions use global variables so that it can accept any number of dimensions 
- Update graphing script 

## 5 March - Global write of crescendo completed

Done by dividing the crescnedo dim1 by number of processors. If i divide using MPI cartesian 
coordinates the results are too small for dim2 i.e. 3 and the warning comes up stating the 
processes are 0. 

## 6-8 March - Graphing script updated

Done by adding a crescendo flag essentially for graphs with 1 IO rate for 1 layer and 1 MPI rank. 
This flag changes the plotting function as well. Can potentially be more streamlined in the future. 

<div>
<img src="imgs/crescendo.pdf" width="500"/>
</div>

Results from 8 full nodes on ARCHER2, averaged 3 times and 10 times in program. 

BP4 has a lot faster parallel write performance, however peak has still not reached with max of 8 nodes. 

<div>
<img src="imgs/crescendo_32nodes.pdf" width="500"/>
</div>

Results from 32 full nodes on ARCHER2, averaged 3 times and 10 times in program. 

BP4 has a lot faster parallel write performance, however peak has still not reached with max of 8 nodes. 





## 7 March - Read HDF5 parallel
https://www.mcs.anl.gov/papers/P4091-0713_2.pdf
Still unable to process parallel reads. 

## 4 March - topology mesh linked to the geometry mesh 
h5dump -d MeshTags/tetra\ marker/topology CRESCENDO_ENGINE_LTMS_order1.h5 > topology.txt
Problem: c is not reading the mesh tag, because perhaps of the space between tetra marker. 





