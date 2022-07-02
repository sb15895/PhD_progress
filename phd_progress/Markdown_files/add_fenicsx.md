## FENICSx 
Dolfinx directory: 
/work/e609/e609/shared/crescendo-nx

## cpp code 
/work/e609/e609/shr203/crescendo-wholeengine-structural-cpp/main.cpp 

```
CMake Error at /mnt/lustre/a2fs-work1/work/y07/shared/utils/core/cmake/3.21.3/share/cmake-3.21/Modules/CMakeTestCXXCompiler.cmake:62 (message):                                                                                                                                   
  The C++ compiler                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                  
    "/opt/cray/pe/craype/2.7.6/bin/CC"                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                  
  is not able to compile a simple test program.     
``` 

Module loadings 
```
module load 
source /work/e609/e609/shared/spack/setup-fenicsx-modules.sh
module avail py-fenics-dolfinx
``` 

## Building crescendo on archer2
```
change cmake files. Export BOOST_DIR=$BOOST_ROOT
cmake -DBoost_INCLUDE_DIR=$BOOST_ROOT/include .
``` 

