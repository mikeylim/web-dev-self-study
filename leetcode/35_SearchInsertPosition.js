// 35. Search Insert Position
// Easy
// 13.8K
// 602
// Companies
// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2
// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1
// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var maxIndex = 0;
    if (nums[maxIndex] === target) {
        return 0;
    }
    for (var i = 1; i <= nums.length; i++) {
        if (nums[maxIndex] < target) {
            maxIndex = i;
        }
        if (nums[maxIndex] === target) {
            return maxIndex;
        }
    }
    return maxIndex;
};
var nums = [1,3,5,6], target = 2
console.log(searchInsert(nums, target));