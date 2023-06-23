/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    // keep subtracting until dividend is greater than 0
    // increment count for each subtraction
    let count = 0;
    let quotient = dividend;
    let div = divisor;
    if (dividend < 0 && divisor < 0) {
        dividend = -dividend;
        divisor = -divisor;
    } else if (dividend < 0) {
        dividend = -dividend;
    } else if (divisor < 0) {
        divisor = -divisor;
    }
    while (dividend - divisor >= 0) {   
        dividend -= divisor;
        count++;
    }
    if (count === -0) {
        return 0;
    } else if (quotient <= 0 && div <= 0) {
        return count;
    } else if (quotient <= 0 || div <= 0) {
        return -count;
    } else {
        return count;
    }
    
    
};

console.log(divide(11111111, 1));
console.log(divide(2, -3));
console.log(divide(-20, 3));
console.log(divide(-20, -3));
