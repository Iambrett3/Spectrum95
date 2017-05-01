#!/usr/bin/env python

def main():
    line = "here is a line of input that will be divided into blocks it's kind of long"
    for word in createBlocks(line):
        print ':'.join(x.encode('hex') for x in word)
    
    # Color test
    #print(''.join(['\033[' + str(x) + 'mFOO' for x in range(0,150)]) +'\033[0m')

def createBlocks(line):
    return line.split()    

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__": main()
