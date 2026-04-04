HASH(

------------------------------------------------------------------------

General Form:\
\
     HASH(alpha_expression, numeric_expression)\
\

------------------------------------------------------------------------

The HASH( numeric function hashes the whole of the first argument to produce a characteristic number which is then reduced modulo the second argument; which will normally be a prime number. Repeated HASH( functions effectively give random numbers in the range 0 to the second argument -1.

Syntax examples:

Bucket = HASH(Key1\$, 131)\
IF (HASH(Index\$, Location) \< New)

 
