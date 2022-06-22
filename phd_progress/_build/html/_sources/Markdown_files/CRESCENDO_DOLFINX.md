## Install CRESCENDO - 17 Feb 


```
export CRESCENDO_DIR=/work/e609/e609/shared/rr-emtm-models/rr-fenics-models/rr-templates
```

```
cmake -DBoost_BOOST_CMAKE=$BOOST_DIR/lib/cmake -DBOOST_ROOT:PATHNAME=$BOOST_DIR -DBoost_LIBRARY_DIRS:FILEPATH=${BOOST_DIR}/lib ..
```
Error: 
```
/work/e609/e609/shr203/crescendo-wholeengine-structural-cpp/Structural.h:23:10: fatal error: ufc.h: No such file or directory

```
Changed structural.h file to include ufcx.h as that is the header file included in ffcx. 

Also changed all ufc_<> elements to ufcx_<> in structural.h 

Now have to change the same in structural.c 

Need to find how to run it using DolfinX. Maybe try other examples. 
