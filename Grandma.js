let exitParameter=false 
let goodbyeChecker= false
function DeafGrandma(input){
    console.log(input)
    let isLowerCase=false
    str=input.replace(/[a-z]/g, "1")
    if (str.includes("1")){isLowerCase=true}
    if (input===""){alert("WHAT?!")}
    else if (isLowerCase === true){alert("SPEAK UP, KID!")}
    else if (isLowerCase === false && input !== "GOODBYE!") {alert("NO, NOT SINCE 1946!")}
    else if (input=== "GOODBYE!"&& goodbyeChecker===false) {alert("LEAVING SO SOON?"); 
    goodbyeChecker=true}
    else if (input=== "GOODBYE!" && goodbyeChecker===true) {alert("LATER, SKATER!");exitParameter=true}

    if (exitParameter===true){return}
    else {
        input=window.prompt()
        DeafGrandma(input)
    }

    
    }
 alert("HEY KID!")
 input=window.prompt()
 DeafGrandma(input)