# zip-cracker
### Submission by Devansh Sehgal for IEEE VIT Recruitments 
# Usage
usage: zipcracker [-h] -i input_file -d dict_file

Crack password protected zip file using dictionary attack

optional arguments:

  -h, --help     show this help message and exit
  
  -i input_file  The path to the zip file
  
  -d dict_file   The path to dictionary file
  
 ## Needs / Modules required
 - argparse
 - zipfile
 
 If the modules are not imported, use:
 ```
 pip install argparse
 ```
 ```
 pip install zipfile
 ```
 In the terminal / command line
 
 ## Limitations
 - Can only use Dictionary attack
 - If the file not in used dictionary, you have to try another
 - Can only crack zip files with some specific encryption
