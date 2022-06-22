## BASIX dependancies 

### xtl install
```
git clone https://github.com/xtensor-stack/xtl
cmake -DCMAKE_INSTALL_PREFIX=$xtl_DIR
make install
```

### xtensor install

```
cmake -DCMAKE_INSTALL_PREFIX=$xtensor_DIR
make install
```

### BLAS install

```
wget http://www.netlib.org/blas/blas-3.10.0.tgz
mkdir build && cd build 
cmake -DCMAKE_INSTALL_PREFIX=$blas_DIR ../
make install 
```

### LAPACK install 
```
git clone git@github.com:Reference-LAPACK/lapack.git
mkdir build
cd build
cmake -DCMAKE_INSTALL_LIBDIR=$LAPACK_DIR cd cd $BLA.. 
make install 
```

### Pybind install 
```
pip install pybind11 --target $WORK_DIR/pybind
```


### basix install - DONE  

```
git clone git@github.com:FEniCS/basix.git
export basix_DIR=? 
cmake -DCMAKE_BUILD_TYPE=Release -DBLAS_LIBRARIES=$blas_DIR/lib -DCMAKE_INSTALL_PREFIX=$basix_DIR -B build-dir -S .
cmake --build build-dir
cmake --install build-dir
``` 

### petsc install 
```
 git clone -b release https://gitlab.com/petsc/petsc.git petsc
./configure --prefix=/work/e609/e609/shr203/opt/gnu/8.0.0/PETSC 
```
https://petsc.org/release/install/install/


then follow on screen commands
installation directory should be $PETSC_DIR

### ffcx installation 
```
git@github.com:FEniCS/ffcx.git
export ufcx_DIR=<>
cmake -DCMAKE_INSTALL_PREFIX=$ufcx_DIR -B build-dir -S cmake/
cmake -B build-dir -S cmake/
cmake --install build-dir
```

### scotch installation 
archer2 modules were not found by cmake?
```
 git clone https://gitlab.inria.fr/scotch/scotch.git
 mkdir build 
 cd build 
 cmake -DCMAKE_INSTALL_PREFIX=$SCOTCH_DIR -DCMAKE_BUILD_TYPE=Release ..
 make -j 
 make install 
 export SCOTCH_ROOT=$SCOTCH_DIR
``` 

### dolfinx install-ND
``` 
module load boost 
git clone https://github.com/FEniCS/dolfinx
cd cpp
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$dolfinx_DIR .. 
cmake -DCMAKE_INSTALL_PREFIX=$dolfinx_DIR \
    -DBoost_NO_BOOST_CMAKE=TRUE \
    -DBoost_NO_SYSTEM_PATHS=TRUE \
    -DBOOST_ROOT:PATHNAME=$BOOST_DIR \
    -DBoost_LIBRARY_DIRS:FILEPATH=${BOOST_DIR}/lib ..

make install
```

```
ERROR:make[2]: *** No rule to make target '/work/y07/shared/libs/core/boost/1.72.0/GNU/9.3/lib/libboost_timer.so.1.72.0', needed by 'dolfinx/libdolfinx.so.0.3.1.0'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:304: dolfinx/CMakeFiles/dolfinx.dir/all] Error 2
``` 

### BOOST install 
```
wget https://boostorg.jfrog.io/artifactory/main/release/1.78.0/source/boost_1_78_0.tar.gz
./bootstrap.sh --prefix=$BOOST_DIR
./b2 
``` 

## Dolfinx re-install 16 FEB 

Boost creates a cmake file in this path: $BOOST_DIR/lib/cmake /work/e609/e609/shr203/opt/gnu/8.0.0/boost/lib/cmake

Trying to point DOLFINX cmake to this file. 

``` 
module load boost 
git clone https://github.com/FEniCS/dolfinx
cd cpp
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$dolfinx_DIR -DBoost_BOOST_CMAKE=$BOOST_DIR/lib/cmake -DBOOST_ROOT:PATHNAME=$BOOST_DIR -DBoost_LIBRARY_DIRS:FILEPATH=${BOOST_DIR}/lib \
-DSCOTCH_ROOT=$SCOTCH_DIR -DCMAKE_POSITION_INDEPENDENT_CODE=ON ..
make install
```

ERROR:relocation R_X86_64_PC32 against symbol `malloc@@GLIBC_2.2.5' can not be used when making a shared object; recompile with -fPIC

### scotch installation 
try it with position independent code on . 
```
 git clone https://gitlab.inria.fr/scotch/scotch.git
 mkdir build 
 cd build 
 cmake -DCMAKE_INSTALL_PREFIX=$SCOTCH_DIR -DCMAKE_BUILD_TYPE=Release -DCMAKE_POSITION_INDEPENDENT_CODE=ON ..
 make -j 
 make install 
 export SCOTCH_ROOT=$SCOTCH_DIR
``` 
