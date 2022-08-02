# Prime-Sieve
Calculates all the Prime numbers of 10^?, as many times as possible in 5 seconds.

Problem/Question:
    
    Write a sieve to count all the prime numbers of 10^? as many times
    as possible in 5 seconds using the base programming languages?

This program was inspired by Dave Plummers youtube videos from his "Software Drag Racing" series:

Dave Plummers Youtube channel ( https://www.youtube.com/c/DavesGarage )

Link to "Software Drag Racing" playlist ( https://www.youtube.com/playlist?list=PLF2KJ6Gy3cZ5Er-1eF9fN1Hgw_xkoD9V1 )

# How it works:

    When setting the bit array we used length//2 to remove the even numbers from the equation.

    The bit array itself represents 3 different pieces of information;
        * The bit, which tells wheather a position is of a prime number(1) or non-prime number(0);
        * The index, which will allow us to locate and change multiple values at once;
        * The represented integer value, which can be calculated by using the equation ( index *2 +1 );


    Settine the size limit to 50:
    * The BitArray gets initialized with len=size/2 (25 in this case) with all elements initialized to 1;

    BitArray =               [ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1 ]
    IndexRepresntation =     [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ]
    IntValueRepresntation =  [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 ]


# Let's go through a quick example:   

    for integerValue in range( from=3, to=sqrt( bits.length ), step=2 ):
        * BIT_ARRAY INDEXING EQUATION is: [ int( integerValue *1.5 ) : END : integerValue ]



-> where the integerValue = 3:

        BitArray[ 4 : END : 3 ] == BitArray indexs to toggle [ 4,  7, 10, 13, 16, 19, 22 ]
                                which represent the integers [ 9, 15, 21, 27, 33, 39, 45 ] (index *2 +1)or(multiples of 3)

                   indexs   [ 0  1  2  3 (4) 5  6 (7) 8  9(10)11 12(13)14 15(16)17 18(19)20 21(22)23 24 ]
      represented integer   [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 ]
              toggle bits   [ 1  1  1  1  0  1  1  0  1  1  0  1  1  0  1  1  0  1  1  0  1  1  0  1  1 ]



-> where the integerValue+2 = 5:

            BitArray[ 7 : END : 5 ] == BitArray indexs to toggle [  7, 12, 17, 22 ]
                                    which represent the integers [ 15, 25, 35, 45 ] (index *2 +1)or(multiples of 5)

                   indexs   [ 0  1  2  3  4  5  6 (7) 8  9 10 11(12)13 14 15 16(17)18 19 20 21(22)23 24 ]
      represented integer   [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 ]
              toggle bits   [ 1  1  1  1  0  1  1  0  1  1  0  1  0  0  1  1  0  0  1  0  1  1  0  1  1 ]



-> where the integerValue+2 = 7:

            BitArray[ 10 : END : 7 ] == BitArray indexs to toggle [ 10, 17, 24 ]
                                     which represent the integers [ 21, 35, 49 ] (index *2 +1)or(multiples of 7)

                   indexs   [ 0  1  2  3  4  5  6  7  8  9(10)11 12 13 14 15 16(17)18 19 20 21 22 23(24)]
      represented integer   [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 ]
              toggle bits   [ 1  1  1  1  0  1  1  0  1  1  0  1  0  0  1  1  0  0  1  0  1  1  0  1  0 ]



We dont need check the integerValue after it exceeds the size of sqrt( len( bitArray ) ).

So now that we have successfully toggled all the necessary bits that represent the NON-PRIME values.

To calculate and retrieve all prime values, use the equation:

            [ index *2 +1 for( index, bit )in enumerate( self._bits ) if bit ]


OUTPUT:

    PASSES:xxxxxx || LIMIT:1000000 || TIME:5.00000 || AVG:0.00001 || COUNT:78_498 || VALID:True
    PRIMES: <list of primes>
