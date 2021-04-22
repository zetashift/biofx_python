#!/usr/bin/env python3
"""
Author : zetashift
Date   : 2021-04-21
Purpose: Transcribe DNA to mRNA
"""

import os
import argparse
from typing import NamedTuple, List, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    out_dir: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to mRNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='DNA',
                        help='Input DNA file',
                        nargs='+',                    # one or more arguments are required
                        type=argparse.FileType('rt')) # our input should be Readable Text

    parser.add_argument('-o',
                        '--out_dir',
                        metavar='DIR',
                        help='Output directory',
                        type=str,
                        default='out')

    args = parser.parse_args()
    return Args(files=args.file, out_dir=args.out_dir)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    num_files, num_seqs = 0, 0

    for fh in args.files:
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        
        for dna in fh:
            out_fh.write(dna.replace('T', 'U'))
            num_seqs += 1

        out_fh.close()
        num_files += 1

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
          f'in {num_files} file{"" if num_files == 1 else "s"} '
          f'to directory "{args.out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
