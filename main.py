#!/usr/bin/python3

from sys import argv
from translate import translate

def main():

    in_file = argv[1]
    if len(argv) > 2:
        extra_mappings_file = argv[2]
        # do nothing with it for now lmao
    
    print(translate(in_file))

if __name__ == '__main__':
    main()