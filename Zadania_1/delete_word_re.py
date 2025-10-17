import sys
import re

def remove_word(file,word):
    with open(file,"r") as f:
        file_data = f.read()
    new_file_data = re.sub(rf'\b{re.escape(word)}\b',"",file_data)
    with open(f"{file}_edited","w") as f:
        f.write(new_file_data)
    

if __name__ == "__main__":
    remove_word(sys.argv[1],sys.argv[2])