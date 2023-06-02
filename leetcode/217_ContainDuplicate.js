/*
217. Contains Duplicate
Easy
9.4K
1.2K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var dup;
    for (var i = 0; i < nums.length; i++) {        
        if (nums.length < 2) {
            return false;
        }
        for (var j = i+1; j < nums.length; j++) {
            if (nums[i] == nums[j]) {
                dup = true;
                return dup;
            } else {
                dup = false;
            }
        }
        console.log("out of the j loop");
        console.log("j -", j);
        console.log("nums[j] -", nums[j]);
    }
    return dup;
};
console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]));
// console.log(containsDuplicate([0,2,3,1,3,4]));
// console.log(containsDuplicate([0,2,8,1,4]));
// console.log(containsDuplicate([0,1,2,3,4]));
// console.log(containsDuplicate([0,1,2,3,1]));