import os,glob
import sys,getopt
import json
import os.path



# Go through all the configs and generate a json file that contains the ids of all the cards in the configs
def main():

    picks = []
    for subdir, dirs , files in os.walk( "." ) :
        for filez in [ f for f in files if f.endswith(".json") ] :
            fullPath = os.path.join( subdir, filez)

            with open( fullPath ) as data_file :
                data = json.load( data_file )
                draftPicks =  data["draftPicks"]

                for pick in draftPicks :
                    options = pick["options"]

                    for card in options :
                        picks.append( card )

    for newCard in set(picks) :
        print newCard


main();
