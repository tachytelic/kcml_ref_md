MAT INV

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = INV(numeric_array1) \[ \[ det \] \[ ,n \]\]\
\
2.      numeric_receiver_array = INV(numeric_array1) \[ \[ det \] \[ ,n \]\]\
\
Where:\
\
     det           = a numeric receiver variable which is assigned the value of the\
               determinant of the numeric_receiver_array.\
\
     n           = a numeric receiver variable which is assigned the value of the\
               normalised determinant of numeric_array1.\
\

------------------------------------------------------------------------

The MAT inverse statement assigns the inverse of numeric_array1 to the numeric_receiver_array. The same array can appear on both sides of the matrix. The reciever array is redimensioned to have the same dimensions as the inverted array which must be a square matrix otherwise an error will occur.

Once the inversion is complete the variables det and n if specified will be set to the determinant and the normalised determinant respectively.

The matrix is inverted using the Gauss-Jordan method with maximum pivoting. It must be square and non-singular.

Syntax examples:

MAT abc = INV(xyz),det,ndet\
abc() = INV(xyz()),dt1,dt2

 
