
from timeit import default_timer


class PrimeSieve( object ):

    _size :int
    _bits :bytearray

    VALID_PRIMES :dict = { 10 : 4,                                          # Size of data with known prime count ( Limit : Prime Count )
                          100 : 25,
                        1_000 : 168,
                       10_000 : 1_229,
                      100_000 : 9_592,
                    1_000_000 : 78_498,
                   10_000_000 : 664_579,
                  100_000_000 : 5_761_455 };


    def __init__( self, SIZE:int ):
        self._size = SIZE;
        self._bits = bytearray( b'\x01' ) *( ( self._size +1 ) //2 );       # Initialize a bytearray with len( _size//2 ) to negate even numbers,
                                                                            # with all bit values initialized to 1.


    def countPrimes( self ) -> int:
        return self._bits.count( b'\x01' );                                 # return sum of bits with a value equal to 1



    def validateResults( self, count:int ) -> bool:
        if( self._size in self.VALID_PRIMES ):                              # If data for bytearray.size exists in VALID_PRIMES
            return  count == self.VALID_PRIMES[ self._size ];               # Compare our result to the data



    def printResults( self, PASSES:int, DURATION:float ) -> None:
        count = self.countPrimes( );
        valid = self.validateResults( count );
        if( valid is None ): print( 'Unvalidated results' );                # Results void if _size is not in VALID_PRIMES 
        print( f'PASSES:{PASSES} || LIMIT:{self._size} || TIME:{DURATION:.5f} || AVG:{DURATION/PASSES:.5f} || COUNT:{count} || VALID:{valid}' );



    def printPrimeValues( self ) -> None:
        print( 'Primes: ', [ e *2 +1 for e, bit in enumerate( self._bits ) if bit ], '\n' )



    def runSieve( self ) -> None :
        BEGIN = 3;
        END = int( self._size **0.5 ) +1;
        STEP = 2;

        for integer in range( BEGIN, END, STEP ):
            if( self._bits[ integer//2 ] ):                                 # integer//2 provides the index location for said integer
                bitslen = len( self._bits ) -( integer *1.5 );              # Gives the remaining array size from the [current:End]
                bitslen = int( bitslen /integer ) +( integer &1 );          # Gives the remaining number of multiples of the current integer
                self._bits[ int(integer *1.5)::integer ] = b'\x00' *bitslen;# Toggle all bits from [first multiple : END : integer] by the number of bits to change




if __name__ == '__main__':
    ELAPSED_TIME = lambda S_TIME: default_timer( ) -S_TIME;

    for limit in [ 1e+1, 1e+2, 1e+3, 1e+4, 1e+5, 1e+6 ]:
        passes = 0;
        N_SECONDS = 5;
        SIZE_OF_SIEVE = int( limit );
        START_TIME = default_timer( );                      # Start TIMER
        
        while( ELAPSED_TIME( START_TIME ) < N_SECONDS ):
            sieve = PrimeSieve( SIZE_OF_SIEVE );
            sieve.runSieve( );
            passes +=1;
            
        DURATION = ELAPSED_TIME( START_TIME );              # End TIMER
        sieve.printResults( passes, DURATION );
        # sieve.printPrimeValues( )