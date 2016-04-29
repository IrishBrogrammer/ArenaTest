import urllib

def downloadCard( card ) : 
    name = card["name"]
    filename = "cards/" + name + ".png"
    url = card["url"]
    urllib.urlretrieve( url , filename )

def main() : 
    card = {}
    card["name"] = "testing"
    card["url"] = "http://wow.zamimg.com/images/hearthstone/cards/enus/original/EX1_621.png"
    downloadCard( card )


main()



