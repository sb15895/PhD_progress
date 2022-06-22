could be used https://www.visitusers.org/index.php?title=Building_on_Ubuntu_12.04 
```
#include "hdf5.h"
#include <stdio.h>
#include <mpi.h>
#include <string.h>
#include <stdlib.h> 
// #define FILE        "~/coding/crescendo-wholeengine-structural-cpp/mesh/CRESCENDO_ENGINE_LTMS_order1.h5"
#define FILE        "CRESCENDO_ENGINE_LTMS_order1.h5"
#define DATASET  "Geometry/geometry/geometry"   
#define DIM0            288626
#define DIM1            3
#define CHUNK0          4
#define CHUNK1          4
#define Nmax            5000

// long double* data_input(void)
void main() 
{
    hid_t           file, space, dset, dcpl, datatype, dataspace, order, size;    /* Handles */
    herr_t          status;
    hsize_t         dims[2] = {DIM0, DIM1},
                    maxdims[2] ,
                    chunk[2] = {CHUNK0, CHUNK1},
                    start[2],
                    count[2];
    int             //wdata[DIM0][DIM1],          /* Write buffer */
                    // wdata2[EDIM0][EDIM1],       /* Write buffer for
                                                   /* extension */
                    **rdata,                    /* Read buffer */
                    ndims,
                    rank, 
                    i, j;
    maxdims[0] =    H5S_UNLIMITED;
    maxdims[1] =    H5S_UNLIMITED;
    /*
    * Open file and dataset using the default properties.
    */
    file = H5Fopen (FILE, H5F_ACC_RDONLY, H5P_DEFAULT);
    dset = H5Dopen (file, DATASET, H5P_DEFAULT);

    // /*
    // * Retrieve dataset creation property list.
    // */
    dcpl = H5Dget_create_plist (dset);

    datatype = H5Dget_type (dset); /* datatype identifier */

    order = H5Tget_order (datatype);
    if (order == H5T_ORDER_LE) printf("Little endian order \n");
    size = H5Tget_size (datatype);
    // printf ("Size is %ld \n", size);
    dataspace = H5Dget_space (dset); /* dataspace identifier */
    /* Find rank and retrieve current and maximum dimension
    * sizes.
    */
    rank = H5Sget_simple_extent_dims (dataspace, dims, maxdims);
    int new_dims[2] = {maxdims[0], maxdims[1]} ; 

    double* ioread = NULL;
    ioread = (double*)malloc(maxdims[0] *maxdims[1] * sizeof(double));

    /*
     * Read the data using the default properties.
     */
    status = H5Dread (dset, H5T_NATIVE_DOUBLE, H5S_ALL, H5S_ALL, H5P_DEFAULT,
                ioread);
    
    for(i= 0; i<maxdims[0]; i++)
    {
        for(j = 0; j<maxdims[1]; j++)
        {
            printf("%lf \n", ioread[i*maxdims[1]+j]);
        }
    }

    status = H5Dclose (dset);
    status = H5Sclose (dataspace);
    status = H5Fclose (file);

    ioread = NULL;

}
```