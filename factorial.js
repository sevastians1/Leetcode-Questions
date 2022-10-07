exports.factorial = function(num) {
   if (num===1){return 1}
     return num*exports.factorial(num-1)
}



// function factorial(num){
// let tempNum=BigInt(1)
// num=BigInt(num)
//     while (num>0){
//     tempNum=BigInt(num*tempNum)
//     num-- 
// }
// return tempNum.toString()
// }