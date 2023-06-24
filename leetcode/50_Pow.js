/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    var total = 1;
    for (let i = 0; i < n; i++) {
        total = total * x;
    }
    return total.toFixed(5);
};

console.log(myPow(2, 10));
console.log(myPow(2.0000, 10));
console.log(myPow(2.10000, 3));


