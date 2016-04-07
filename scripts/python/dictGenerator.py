import sys
import json
import unirest
import os,glob
import os.path


filename = str( sys.argv[0])

with open( filename ) as data_file :
    data = json.load( data_file )

    print data
