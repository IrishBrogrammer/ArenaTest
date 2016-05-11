import urllib
import json 
import sys

def downloadCard( cardName , cardURL ) : 
    filename = "cards/" + cardName + ".png"
    urllib.urlretrieve( cardURL , filename )

def main() : 
    card = {}
    card["name"] = "testing"
    card["url"] = "http://wow.zamimg.com/images/hearthstone/cards/enus/original/EX1_621.png"
    downloadCard( card )



def downloadMissingCards( missingCards , urlDict ) :

    for card in missingCards :
        if card in urlDict :
            downloadCard( card , urlDict[card] )
        else :
            print "Could not find" + card 
    

def generateMissingCardsList( validCards , cachedCards ) :
    missingCards = []
    missingCards = set(validCards) - set(cachedCards)
    return missingCards

def downloadCards( validCardsPath , downloadedCardsPath ,  cardDictPath   ) :
    
    validCards = []
    cachedCards = []
    urlDict = []
    
    with open( validCardsPath ) as data_file : 
        validCards = json.load( data_file )
    
    with open( downloadedCardsPath ) as cached_file : 
        cachedCards = json.load( cached_file )
        
    missingCards = generateMissingCardsList( validCards , cachedCards )  
    
    print " The following cards are missing " 
    for card in missingCards :
        print card
    
    print " Attempting to download missing cards " 
    with open( cardDictPath ) as url_file : 
        urlDict = json.load( url_file )
     
    downloadMissingCards( missingCards , urlDict )
    
   # with open( cardDictPath ) as card_file : 
    #    cardDict = json.load( cardDict )
        
        


validCardsPath = str( sys.argv[1])
cachedCardsPath = str( sys.argv[2] )
cardDict = str( sys.argv[3] )
downloadCards( validCardsPath , cachedCardsPath , cardDict )



