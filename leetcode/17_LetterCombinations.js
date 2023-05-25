/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var dict = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    };
    var result = [''];
    for (let digit of digits) {
        var letters = dict[digit];
        var temp = [];
        for (let letter of letters) {
            for (let str of result) {
                temp.push(str + letter);
            }
        }
        result = temp;
    }
    return(result);
};

console.log(letterCombinations("23"));