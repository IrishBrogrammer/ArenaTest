import os,glob
import sys,getopt
import json
import os.path

def testPick( pick ) :

    options = pick["options"]

    if len( options ) != 3 :
        print "One of the draft picks does not have 3 options"
        return False

    if options.count(pick["answer"]) != 1 :
        print " Answer : " + pick["answer"] + " was not found in list"
        return False

    return True

def runTest( draft ) :
    for pick in draft :
        if testPick( pick ) == False :
            return False
    return True

def testFile( fileName ) :
    print " Testing File " + fileName

    with open(fileName) as data_file :
        data = json.load( data_file)
        print "Testing " + data["name"]
        return runTest( data["draftPicks"])

def main() :
    fileName = str( sys.argv[1])

    if ( testFile( fileName ) ) :
        print "All configs are ok"
    else :
        print " Validation failed on file " + fileName
main();
