import requests as r
import argparse
import os 

def checkStatus(file,output):
    with open(file,"r") as check:
        for line in check:
            try:
                if r.get(line.strip()).status_code == 200:
                    with open(f"{output}", "a") as active:
                        active.write(line.strip())
                        active.write("\n")
            except:
                pass

parser = argparse.ArgumentParser(description='Url tookkit')
parser.add_argument('-f',required=True ,dest="file", metavar='[Check if url in file are active(200).]', type=str, nargs=1,help='Input a file make ure the line are sperated ')
parser.add_argument('-o',required=True,dest="outputFile", metavar="[Output file]", type=str, nargs=1, help='Will place new urls in this file.')

args = parser.parse_args()

if __name__ == "__main__":
    checkStatus(args.file[0], args.outputFile[0])

