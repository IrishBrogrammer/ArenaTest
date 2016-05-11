import os
import os.path
import sys
import json
# Go through a sub folder of images and generate a json list of all the card names
# so we have a list of cards already downloaded 

def main( cardFolder , outputFile ) :
    downloadedCards = []
    for subdir,dirs,files in os.walk( cardFolder ) : 
        for filez in [ f for f in files if f.endswith(".png") ] :     
            downloadedCards.append( filez[:-4])
    
    with open( outputFile , 'w' ) as f : 
        f.write( json.dumps( downloadedCards , sort_keys=True , indent=4 , separators=(',',':') ))
    
    
    
cardFolder = str( sys.argv[1] )
outputFile = str( sys.argv[2] )    
main( cardFolder , outputFile )
