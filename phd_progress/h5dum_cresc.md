```
shr203@ln03:/work/e609/e609/shr203/crescendo-wholeengine-structural-cpp/mesh> 
HDF5 "CRESCENDO_ENGINE_LTMS_order1.h5" {
GROUP "/" {
   GROUP "Geometry" {
      GROUP "geometry" {
         DATASET "geometry" {
            DATATYPE  H5T_IEEE_F64LE
            DATASPACE  SIMPLE { ( 288626, 3 ) / ( 288626, 3 ) }
         }
      }
   }
   GROUP "MeshTags" {
      GROUP "tetra marker" {
         DATASET "Values" {
            DATATYPE  H5T_STD_I32LE
            DATASPACE  SIMPLE { ( 888646, 1 ) / ( 888646, 1 ) }
         }
         DATASET "topology" {
            DATATYPE  H5T_STD_I64LE
            DATASPACE  SIMPLE { ( 888646, 4 ) / ( 888646, 4 ) }
         }
      }
      GROUP "triangle marker" {
         DATASET "Values" {
            DATATYPE  H5T_STD_I32LE
            DATASPACE  SIMPLE { ( 579315, 1 ) / ( 579315, 1 ) }
         }
         DATASET "topology" {
            DATATYPE  H5T_STD_I64LE
            DATASPACE  SIMPLE { ( 579315, 3 ) / ( 579315, 3 ) }
         }
      }
   }
}
}

```