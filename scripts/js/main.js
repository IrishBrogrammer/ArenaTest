function loadJSON( callback ){

  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");

  xobj.open( 'GET', "jsonFile.json" , true );
  xobj.onreadystatechange = function() {

    if( xobj.readyState == 4 && xobj.status == "200" )
    {
        callback( xobj.responseText);
    }
  };

  xobj.send(null );
}


function usage()
{
  loadJSON( onJsonLoaded );
}

function onJsonLoaded( response ){
    var actualJson = JSON.parse( response );
}



function TestCase()
{
    var testData = '[{"Blue" : "is ok", "red" : " is wrong"}]';
    var parsedData = JSON.parse( testData );  
}
