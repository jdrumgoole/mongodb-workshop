#!/usr/bin/env python
"""
We have directories with a set of files in number format.
Assuming the numbers are prefixes.

"""

from argparse import ArgumentParser
import re
import glob
from collections import OrderedDict
import os

if __name__ == "__main__":

    parser = ArgumentParser()

    #'{:0>3d}'.format( 50 )
    parser.add_argument( "--pattern", default='{:0>2d}', help="Format string used to detect filenames")
    parser.add_argument( "--hole", type=int, help="Hole location")
    parser.add_argument( "--holesize", type=int, default=1, help="How big a gap to make")
    parser.add_argument( "files", nargs="*", help="Residue arguments")

    args = parser.parse_args()

    hole_str = args.pattern.format( args.hole)
    #print(hole_str)
    matcher = re.compile( "^[0-9]+_.*" )
    match_map = OrderedDict()
    for f in args.files:
        filename = os.path.basename(f)
        if matcher.match(filename):
            ( id, name) = filename.split( "_")
            if id in match_map:
                print( "Duplicate file ID:{} and {}".format( match_map[id], filename))
            else:
                match_map[ id ] = ( f, filename )

    

    for ( _,f)in match_map.items():
        print(f[1])