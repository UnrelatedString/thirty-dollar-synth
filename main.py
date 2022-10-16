#!/usr/bin/python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: (C) 2022 UnrelatedString <https://github.com/UnrelatedString>

from sys import argv
from translate import translate

def main():

    in_file = argv[1]
    if len(argv) > 2:
        instrument = argv[2]
    else:
        instrument = 'stopposting'
        
    print(translate(in_file, instrument))

if __name__ == '__main__':
    main()