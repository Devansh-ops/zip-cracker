import argparse
import zipfile
#from tqdm import tqdm

def extractFile(zfile, password):
    with zipfile.ZipFile(zfile) as zFile:
        try:
            password_encoded = bytes(password.encode('utf-8'))
            zFile.setpassword(password_encoded)
            zFile.testzip()
            print ("[+] Password Found:", password)
            zFile.close()
            exit(0)
        except RuntimeError:
            pass

def main():
    parser = argparse.ArgumentParser(prog="zipcracker",description="Crack password protected zip file using dictionary attack")

    parser.add_argument('-i',metavar="input_file", type=str, help="The path to the zip file",required=True)
    parser.add_argument('-d',metavar="dict_file", type=str, help="The path to dictionary file",required=True)
    args = parser.parse_args()

    try:
        zfile = args.i
        dfile = open(args.d)

        for line in dfile.readlines():
            pw = line.strip("\n")
            print(pw)
            extractFile(zfile,pw)
    except:
        pass
    finally:
        dfile.close()

if __name__ == '__main__':
    main()
