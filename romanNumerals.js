exports.toRoman = function(input) {
// function toRoman(input){
    if(input===0){return}
arr= input.toString().split("")
sv=0
mv=0
bv=0
length = arr.length-1
arr= input.toString().split("")
for (let i = 0; i<arr.length; i++){
    let tempValue= String(+arr[i]*Math.pow(10, length))
    
    length--
    if (tempValue<=10){sv="I";mv="V";bv="X"}
    else if(tempValue>10&& tempValue<100){sv="X";mv="L";bv="C"}
    else if (tempValue>=100 && tempValue<1000){sv="C";mv="D";bv="M"}
    else {sv="M";mv="BIG V";bv="BIG X"}
    switch(+arr[i]){
        case 1:
            arr[i]=sv
            break
        case 2:
            arr[i]=sv+sv
            break
        case 3:
            arr[i]=sv+sv+sv
            break
        case 4:
            arr[i]=sv+mv
            break
        case 5:
            arr[i]=mv
            break
        case 6:
            arr[i]=mv+sv
            break
        case 7:
            arr[i]=mv+sv+sv
            break
        case 8:
            arr[i]=mv+sv+sv+sv
            break
        case 9:
            arr[i]=sv+bv
            break
        case 0:
            arr[i]=""
            break                            
                    }
}
return arr.join("")

};


