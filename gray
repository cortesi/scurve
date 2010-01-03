#!/usr/bin/env python
from scurve import utils

def main():
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(
                usage = "%prog [options] output",
                version="%prog 0.1",
            )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Please specify the bit width of the desired gray code.")

    width = int(args[0])
    for i in range(2**width):
        print str(utils.bits(utils.graycode(i), width))[1:-1]


main()
