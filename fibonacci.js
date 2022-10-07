const fibonacci = (num) => {
    let arr=[1,0]
let counter=0
while (counter!==num){
let oldValue=arr[1]+arr[0]
arr.unshift(oldValue)
arr.pop()
counter++
}
return arr[1]
}

module.exports = {fibonacci}
