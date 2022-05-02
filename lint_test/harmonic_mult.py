#! /usr/bin/env python3.9
def harmonic( n : int ): 
    """ Writes out the first n numbers in the harmonic series, one in each line, and finally their sum.  All the numbers should be written out rounded to the forth decimal digit. """
    oUtPuT_sUm = 0
    output = [ ]
    for i in range(1,n+1):
        oUtPuT_sUm += int(1/i)
        output += [round(1/i,4)] 

    return output   +   [ "Sum of series: " + str(round(oUtPuT_sUm,4))]

