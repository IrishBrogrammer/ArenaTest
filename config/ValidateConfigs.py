import os,glob
import sys,getopt
import json
import os.path

# Test that a draft pick has at least 3 options and the answer for the pick is in the options provided
def testPick( pick ) :

    options = pick["options"]

    if len( options ) != 3 :
        print "One of the draft picks does not have 3 options"
        return False

    if options.count(pick["answer"]) != 1 :
        print " Answer : " + pick["answer"] + " was not found in list"
        return False

    return True

# Test all the picks in a draft to ensure its a valid draftPicks
def runTest( draft ) :
    for pick in draft :
        if testPick( pick ) == False :
            return False
    return True

# Load a json file and test if it is a valid draft
def testFile( fileName ) :
    with open(fileName) as data_file :
        data = json.load( data_file)
        return runTest( data["draftPicks"])

# Entry point of application.
def main() :
    hasPassedAll = True

    for subdir, dirs , files in os.walk( "TestAcc" ) :
        for filez in [ f for f in files if f.endswith(".json") ] :
            fullPath = os.path.join( subdir, filez)
            if  testFile( fullPath ) == False :
                print "File : " + fullPath + " has failed tests"
                hasPassedAll = False

    if hasPassedAll :
        print " All tests passed "

main();
