import sys
import json
import unirest

def getCardInfo( cardObj ) :
    name = cardObj["name"]
    url  = cardObj["img"]
    return str( name ) + " : " + str( url )


def getCard() :
    response = unirest.get( "https://omgvamp-hearthstone-v1.p.mashape.com/cards/ysera",
                            headers={
                            "X-Mashape-Key" : "INSERT_KEY",
                            "Accept" : "application/json"
                            })
    return response


def getAllCards() :
    response = unirest.get( "https://omgvamp-hearthstone-v1.p.mashape.com/cards",
                            headers={
                            "X-Mashape-Key" : "INSERT_KEY",
                            "Accept" : "application/json"
                            },
                            params={
                            "collectible" : 1
                            })
    return response


def getYseraTest( outputPath ) :
    print " Getting Ysera "
    response = getCard()
    responseDict = response.body[0]

    with open( outputPath , 'w' ) as f :
         f.write( getCardInfo( responseDict ))

    print " got Ysera "


print "Hello World "

outputPath = str( sys.argv[1] )
response  = getAllCards()

setsToPrint = [ "Classic","Naxxramas","The League of Explorers","Basic","The Grand Tournament","Goblins vs Gnomes"]

print "Size " + str( len( response.body ) )


testSet = response.body["Classic"]

print len(testSet)


for set in setsToPrint :
    print set
    print len(response.body[set])



with open( outputPath , 'w' ) as f :
    f.write( str( response.body ) )




print "Bye world "
