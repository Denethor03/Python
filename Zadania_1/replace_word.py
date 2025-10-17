import json
import sys


def replace_word(file,words):
    with open(words) as f:
        dict = json.load(f)
    with open(file,"r") as f:
        content = f.read()
    for key,value in dict.items():
        content = content.replace(key,value)
    with open(f"{file}_edited","w") as f:
        f.write(content)

if __name__ == "__main__":
    replace_word(sys.argv[1],sys.argv[2])