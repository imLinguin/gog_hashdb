#!/usr/bin/env python3

import os 
import sys
import zipfile

def main():
    parameters = sys.argv[1:]
    while parameters:
        file = parameters.pop()
        if not os.path.exists(file):
            print(f"File {file} not found")
            continue 

        print("\nParsing", file, '\n')
        zip = zipfile.ZipFile(file, "r")
        name = zip.namelist()[0] # There is one file

        with zip.open(name, 'r') as f:
            f.seek(0)
            header_1 = f.read(4)
            header_2 = f.read(4)
            header_3 = f.read(4)

            part1 = int.from_bytes(header_1, "little") # Unknown puprose 
            part2 = int.from_bytes(header_2, "little") # Unknown purpose
        
            number_of_files = int.from_bytes(header_3, "little")      

            for file in range(number_of_files):
                file_name = f.read(1024).decode().replace("\\", "/")
                checksum = f.read(32)
                print(file_name, checksum.decode())


if __name__ == "__main__":
    main()