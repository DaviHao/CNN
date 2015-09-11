# Author: Haotian ZHANG
#
# License: BSD 3 clause
import util  
import sys,os
import getopt
import subprocess
import json
import fileinput
import random
import math
import operator
from random import shuffle  

#usage: python generateReviewLabel.py --input=folder --label=label --output=labeledReview

def usage():
	print """python generateReviewLabel.py
    --help
    --input=folder
    --label=label of this folder
    --output=labeledReview
    """

def error():
    usage()
    sys.exit(-1)


def cmdProcess(argv):
    myArgs={}
    try:
        opts, args = getopt.getopt(argv,"h",["help", "input=","output="])
    except getopt.GetoptError:
        error()
    for opt, arg in opts:
        if opt in ("--help","-h"):
            usage()
            sys.exit()
        else:
            opt="".join(opt[2:])
            myArgs[opt]=arg
    return myArgs




if __name__ == "__main__":
    argvNum=1
    if len(sys.argv)<=argvNum:  
        error()
    myArgs=cmdProcess(sys.argv[1:])

    inputFile=myArgs['input']
    outputFile=myArgs['output']



    print("Read files from this raw review sentences")

    outFile=open(outputFile,'w')

    reviewList = []
   
    with open(inputFile,'r') as f:
        while True:
            readData=f.readline()
            if not readData:
                break
            label =  int(readData)
            sentence = f.readline()
            reviewPair = (label, sentence)
            reviewList.append(reviewPair)
    shuffle(reviewList)
    print len(reviewList)
   
    for i in range(20): 
        print reviewList[i]
    #print reviewList[2]
    #print reviewList[4]
    #print reviewList[8]
    # for pair in reviewList:
    for pair in reviewList:
        (label, sentence) = pair
        outFile.write(str(label)+"\n")
        outFile.write(sentence)

    outFile.close()


