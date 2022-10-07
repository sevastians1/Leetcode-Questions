
alert("HEY KID")
function Grandma(){
    let flipperValue = true
    let goodbyes = 0
while ( flipperValue ) {

    let input = window.prompt()

    if ( input === "" ) {
        alert("WHAT!?")
    }
    else if ( input === "GOODBYE!" ) {
        goodbyes=goodbyes+1}
    else if ( input.toUpperCase() !== input ) {
        alert("SPEAK UP, KID!")
    }
    else if ( input.toUpperCase() === input ) {
        alert('NO, NOT SINCE 1946!')
    }

    if ( input == "GOODBYE!" && goodbyes<2){
              alert("LEAVING SO SOON?")}

    
    else if ( goodbyes == 2 ) {
            alert("LATER, SKATER!")
            flipperValue = false
        }
    }
}
Grandma()