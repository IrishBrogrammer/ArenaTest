
$("p").click( function ( event ) {

  var cardID = $(this).attr( 'id');

});

var correctCard = "Brian";

function OnCorrectCardSelected()
{
   // Set the text to say correct
}

function OnIncorrectCardSelected()
{
  // set the text to say incorrect
}

function SetCardHighlights()
{
  // Put a green highlight around the correct card and a red one around the incorrect cards

}

function runCardSelection( selectedCard )
{
    if ( selectedCard == correctCard )
    {
        OnCorrectCardSelected();
    }
    else
    {
        OnIncorrectCardSelected();
    }

    SetCardHighlights();
}
