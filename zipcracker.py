import argparse
<<<<<<< Updated upstream
import os
import sys
=======
>>>>>>> Stashed changes
import zipfile
#from tqdm import tqdm
from multiprocessing import Process

def extractFile(zfile, password):
    with zipfile.ZipFile(zfile) as zFile:
        try:
            password_encoded = bytes(password.encode('utf-8'))
            zFile.setpassword(password_encoded)
            zFile.testzip()
            print ("[+] Password Found: " + password + '\n')
            exit(0)
        except RuntimeError:
            pass
def main():
    parser = argparse.ArgumentParser(prog="zipcracker",description="Crack password protected zip file using dictionary attack")

    parser.add_argument('-i',metavar="input_file", type=str, help="The path to the zip file",required=True)
    parser.add_argument('-d',metavar="dict_file", type=str, help="The path to dictionary file",required=True)
    args = parser.parse_args()

    try:
        #zfile = zipfile.ZipFile(args.i)
        zfile = args.i
        dfile = open(args.d)
        #process = []
        #n_words = len(list(dfile))
        #print("Total passwords to test:", n_words)
        for line in dfile.readlines():
            pw = line.strip("\n")
            print(pw)
            '''
            p = Process(target=extractFile, args=(zfile,pw))
            p.start()
            p.join()
            '''
            extractFile(zfile,pw)
    except:
        pass
    finally:
        '''
        zfile.close()
        '''
        dfile.close()
'''
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
'''
if __name__ == '__main__':
    main()
