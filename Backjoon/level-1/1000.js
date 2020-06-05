const readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


let stringInput = readline.readline();
let numberList = stringInput.split(" ")
var total = 0;

for (let i of numberList) {
    total += Number(i);
}

console.log(total);