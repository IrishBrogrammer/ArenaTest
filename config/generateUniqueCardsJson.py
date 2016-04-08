import os,glob
import sys,getopt
import json
import os.path


# Go through all the configs and generate a json file that contains the ids of all the cards in the configs
def main( outputPath ):

    picks = []
    for subdir, dirs , files in os.walk( "TestAcc" ) :
        for filez in [ f for f in files if f.endswith(".json") ] :
            fullPath = os.path.join( subdir, filez)

            with open( fullPath ) as data_file :
                data = json.load( data_file )
                draftPicks =  data["draftPicks"]
                for pick in draftPicks :
                    options = pick["options"]
                    for card in options :
                        picks.append( card )


    uniqueCards = []
    for cardID in set(picks) :
        uniqueCards.append(str(cardID) )

    with open( outputPath , 'w' ) as f :
        f.write( json.dumps( uniqueCards , sort_keys=True , indent=4 , separators=(',',':') ))


outputPath = str( sys.argv[1] )
main( "allCards.json" )
