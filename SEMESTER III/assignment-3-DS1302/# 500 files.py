# 500 files

import random
import os

letters= "qwertyuiopasdfghjklzxcvbnm"

def  randomchar():
    out_str=""
    out_str="".join(random.choice(letters) for i in range(20))
    return out_str

def create_txt():
    try:
        os.mkdir("file500")
    except:
        print("press F")
    for i in range(500):
        filenamer= "file500/f{}.txt".format(i)
        out_file=open(filenamer,"w")
        for i in range(20000):
            out_file.write(randomchar()+ "\n")
        out_file.close()

create_txt()


