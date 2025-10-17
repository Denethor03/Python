import os
import sys

def count_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)): 
            files.append(file)
            print(file)
    print(f"{len(files)} file(s) found")
   
    
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("No path provided")
    else:
        count_files(sys.argv[1])

