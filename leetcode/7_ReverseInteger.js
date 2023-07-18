// Given a signed 32-bit integer x, return x with its digits reversed.
// If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

// Example 1:

// Input: x = 123
// Output: 321
// Example 2:

// Input: x = -123
// Output: -321
// Example 3:

// Input: x = 120
// Output: 21
 

// Constraints:

// -231 <= x <= 231 - 1

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    // negative
    if (x < 0) {
        var negative = true;
        x = x * -1;
    }
    var reversed = 0;
    var lastdigit = 0;
    
    if (x < 10) { // one digit
        reversed = x;
    } else if ((x >= Math.pow(2, 31) - 1) || x <= Math.pow(-2, 31)) { // constraint
        return 0;
    } else {    // two or more digits
        while (x > 0) {
            lastdigit = x % 10;
            reversed = reversed * 10 + lastdigit;
            x = Math.floor(x /10);
        }
    }
    if (reversed >= Math.pow(2, 31) - 1 || reversed <= Math.pow(-2, 31)) {
        return 0;
    } 

    if (negative) {
        return -reversed;
    } else {
        return reversed;
    }
};

// console.log(reverse(123));
console.log('reversed - ', reverse(-123));
console.log('reversed - ', reverse(Math.pow(2, 31)));
console.log('reversed - ', reverse(-2));
console.log('reversed - ', reverse(10));