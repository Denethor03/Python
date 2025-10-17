import os
import sys

def count_files(path):
    total_count = 0
    for file in os.listdir(path):
        full_path = os.path.join(path,file)
        if os.path.isfile(full_path): 
            print(full_path)
            total_count+=1
        elif os.path.isdir(full_path):
            new_path = os.path.join(full_path)
            total_count+=count_files(new_path)
    return total_count
            
    
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("No path provided")
    else:
        print(f"{count_files(sys.argv[1])} file(s) found")

