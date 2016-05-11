import sys
import json
import unirest

def getCardInfo( cardParent , cardObj ) :
    NewCard = {}
    cardName = cardObj["name"]
    NewCard[cardName] = cardObj["img"]
    cardParent[cardName] = cardObj["img"]
    return cardParent

def getCard() :
    response = unirest.get( "https://omgvamp-hearthstone-v1.p.mashape.com/cards/ysera",
                            headers={
                            "X-Mashape-Key" : "INSERT_KEY",
                            "Accept" : "application/json"
                            })
    return response

def downloadAllCards() :
    response = unirest.get( "https://omgvamp-hearthstone-v1.p.mashape.com/cards",
                            headers={
                            "X-Mashape-Key" : "NdFTbiO6tkmshspvsGbFeKdpKGqip1nEdkBjsnTUctqfAU0Fq3",
                            "Accept" : "application/json"
                            },
                            params={
                            "collectible" : 1
                            })
    return response


def getYseraTest( outputPath ) :
    response = getCard()
    responseDict = response.body[0]

    with open( outputPath , 'w' ) as f :
         f.write( getCardInfo( responseDict ))


def getAllCards( outputPath ) :
    response = downloadAllCards()

    setsToPrint = [ "Classic","Naxxramas","The League of Explorers","Basic","The Grand Tournament","Goblins vs Gnomes","Blackrock Mountain","Whispers of the Old Gods"]

    for set in response.body :
        print set

    cards = {}
    for set in setsToPrint :
        print set
        print len(response.body[set])
        for card in response.body[set] :
            cards =  getCardInfo( cards , card )

    with open( outputPath , 'w' ) as f :
        f.write( json.dumps( cards , sort_keys=True , indent=4 , separators=(',',':') ))



outputPath = str( sys.argv[1] )
getAllCards( outputPath )
