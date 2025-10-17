import sys

def remove_word(file,word):
    with open(file,"r") as f:
        file_data = f.read()
    new_file_data = file_data.replace(word,"")
    with open(f"{file}_edited","w") as f:
        f.write(new_file_data)
    

if __name__ == "__main__":
    remove_word(sys.argv[1],sys.argv[2])