import argparse
import os
import sys
###############
def main():
    parser = argparse.ArgumentParser(prog="zipcracker",description="Crack password protected zip file")

    parser.add_argument('-i',metavar="input_file", type=str, help="The path to the zip file",required=True)
    parser.add_argument('-t',metavar="type",type=str,help="The type of attack", default='d')
    parser.add_argument('-d',metavar="dict_file", type=str, help="The path to dictionary file")
    args = parser.parse_args()

    print(args)

    input_path = args.i
###############
'''
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
'''
if __name__ == '__main__':
    main()
