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
import nltk.data
  

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
        opts, args = getopt.getopt(argv,"h",["help", "input=","output=", "label="])
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

def  extractSentence(data):

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(data)


if __name__ == "__main__":
    argvNum=1
    if len(sys.argv)<=argvNum:  
        error()
    myArgs=cmdProcess(sys.argv[1:])

    inputFolder=myArgs['input']
    label=myArgs['label']
    outputFile=myArgs['output']


    print("Download punkt from NLTK")
    nltk.download('punkt')

    print("Read files from this folder")
    
    #Deveptive review is 0 and truthful review is 1
    flag = 1
    if "deceptive" in label:
        flag = 0

    maxLength = 0
    outFile=open(outputFile,'w')
    for subdir, dirs, files in os.walk(inputFolder):
        for eachfile in files:
            if ".txt" in eachfile:
                with open(os.path.join(subdir, eachfile),'r') as f:
                    readData=f.read()
                sentences = extractSentence(readData)
                # print sentences
                for sentence in sentences:
                    sentence = sentence.strip()
                    sentence = util.clean_text(sentence)
                    sentenceLen = len(sentence.split())
                    if sentenceLen > maxLength:
                        maxLength = sentenceLen
                    if sentence != '' and sentenceLen > 1 and sentenceLen < 100:
                        outFile.write(str(flag) + "\n" + sentence)
    print "Max length of sentence is " +str(maxLength)
    outFile.close()


