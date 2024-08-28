import argparse

def rewrite(file, output):
    with open(file,"r") as file:
        for line in file:
            link = f"https://{line}"
            with open(f"{output}","a") as newFile:
                newFile.write(link)

parser = argparse.ArgumentParser(description='Url tookkit')
parser.add_argument('-f', required=True, dest="file", metavar='[Puts https:// in front of links]', type=str, nargs=1,help='Input a file make ure the line are sperated this will change link like this google.com to this https://google.com')
parser.add_argument('-o',required=True,dest="outputFile", metavar="[Output file]", type=str, nargs=1, help='will place new urls in this file.')

args = parser.parse_args()

if __name__ == "__main__":
    rewrite(args.file[0], args.outputFile[0])

