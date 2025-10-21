/*
Write a function that takes in a string of one or more words, and returns the same string,
but with all words that have five or more letters reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"


*/

function spinWords(string) {
	const words = string.split(" ");
	let newWords = "";
	for (let word of words) {
		if (word.length >= 5) {
			word = [...word].reverse().join("");
		}
		newWords += word + " ";
	}

	return newWords.trimEnd();
}

let str1 = "Hey fellow warriors";
let str2 = "This is a test";
let str3 = "This is another test";
let str4 = "Welcome";

console.log(spinWords(str1));
console.log(spinWords(str2));
console.log(spinWords(str3));
console.log(spinWords(str4));
