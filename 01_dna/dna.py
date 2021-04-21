#!/usr/bin/env python3
"""
Author : zetashift 
Date   : 2021-04-20
Purpose: Tetranucleotide frequency
"""

import argparse, os
from typing import NamedTuple, Tuple

class Args(NamedTuple):
    """ Command-line arguments """
    dna: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='Input DNA Sequence')

    args = parser.parse_args()
    
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)

def count(dna: str) -> Tuple[int, int, int, int]:
    return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args() # If this call succeeds, the arguments are valid and ready to use
    # print(args.dna) The name of the argument will also be an attribute name to `args` 
    count_a, count_c, count_g, count_t = count(args.dna)
    print(f'{count_a} {count_c} {count_g} {count_t}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
