
function Bottles(start){
    
     while (start>2){
        let newBottle=start-1
        console.log(`${start} bottles of beer on the wall, ${start} bottles of beer. \
        Take one down and pass it around, ${newBottle} bottles of beer on the wall.`)
        start=newBottle    
}

    console.log( `1 bottle of beer on the wall, 1 bottle of beer. \
    Take one down and pass it around, no more bottles of beer on the wall. \n`+
    `No more bottles of beer on the wall, no more bottles of beer.\
    Go to the store and buy some more, 99 bottles of beer on the wall.`)

}
Bottles(99)
function BottlesNoLoops(start){
if (start===1){
console.log( `1 bottle of beer on the wall, 1 bottle of beer. \
Take one down and pass it around, no more bottles of beer on the wall. \n`+
`No more bottles of beer on the wall, no more bottles of beer.\
Go to the store and buy some more, 99 bottles of beer on the wall.`)
return " "
}
let newBottle=start-1
console.log(`${start} bottles of beer on the wall, ${start} bottles of beer. \
Take one down and pass it around, ${newBottle} bottles of beer on the wall.`)
start=newBottle
BottlesNoLoops(newBottle)
return " "

}


BottlesNoLoops(99)
