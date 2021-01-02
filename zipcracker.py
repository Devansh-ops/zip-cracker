import argparse
import zipfile

def extractFile(zfile, password):
    with zipfile.ZipFile(zfile) as zFile:
        try:
            password_encoded = bytes(password.encode('utf-8'))
            zFile.setpassword(password_encoded)
            zFile.extractall()
            print ("[+] Password Found:", password)
            exit(0)
        except SystemExit:
            exit()
        except:
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
            extractFile(zfile,pw)
        print("[-] Password not in wordlist. Try a different wordlist!!")
    except SystemExit:
        exit()
    except:
        print("There was some error")
        parser.print_help()
        exit()

if __name__ == '__main__':
    main()
