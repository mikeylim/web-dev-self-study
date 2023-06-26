/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    var root;

    // finding perfect square
    for (let i = 2; i < x; i++) {
        if (i * i == x) {
            return i;
        } else {
            
        }
    }

    for (let i = 2; i < x; i++) {
        if ((i-1) * (i-1) > x) {
            root = (i-1);
        } else {
            root = (i+1);
        }
    }

    return root;
    

};

console.log(mySqrt(2));
console.log(mySqrt(3));
console.log(mySqrt(5));
console.log(mySqrt(10));
console.log(mySqrt(4));
console.log(mySqrt(9));
console.log(mySqrt(16));
console.log(mySqrt(25));
console.log(mySqrt(100));
console.log(mySqrt(88));