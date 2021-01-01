import argparse
#import os
#import sys
import zipfile
from multiprocessing import Process

def extractFile(zfile, password):
    try:
        print("trying",password)
        zfile.extractall(pwd=password)
        print('[+] Found Password:',password)
        exit(0)
    except:
        pass

def main():
    parser = argparse.ArgumentParser(prog="zipcracker",description="Crack password protected zip file")

    parser.add_argument('-i',metavar="input_file", type=str, help="The path to the zip file",required=True)
    parser.add_argument('-t',metavar="type",type=str,help="The type of attack", default='d')
    parser.add_argument('-d',metavar="dict_file", type=str, help="The path to dictionary file")
    args = parser.parse_args()

    try:
        zfile = args.i
        dfile = open(args.d)
        process = []

        for line in dfile.readlines():
            pw = line.strip("\n")
            p = Process(target=extractFile, args=(zfile,pw))
            p.start()
            p.join()
    finally:
        dfile.close()

if __name__ == '__main__':
    main()
