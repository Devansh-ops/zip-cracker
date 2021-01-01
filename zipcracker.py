import argparse
import os
import sys
###############
parser = argparse.ArgumentParser(prog="zipcracker",description="Crack password protected zip file")

parser.add_argument('Path', metavar='path', type=str,help="The path to the list")

args = parser.parse_args()

input_path = args.Path
###############
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
