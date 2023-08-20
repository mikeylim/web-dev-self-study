// 283. Move Zeroes
// Easy
// 14.8K
// 376
// Companies
// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

 

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]
 

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1
 

// Follow up: Could you minimize the total number of operations done?
// Accepted
// 2.4M
// Submissions
// 3.9M
// Acceptance Rate
// 61.4%

#include <stdio.h>

#include <stdio.h>

void moveZeroes(int* nums, int numsSize) {
    if (numsSize == 1) {
        return;
    }

    int zeroCount = 0;
    // count how many zeroes are in array
    // swap
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            zeroCount++;
        }
    }

    int i = 0;
    int counter = 0;
    
    while (i < numsSize) {
        if (nums[i] != 0) {
            nums[counter] = nums[i];
            counter++;
            i++;
        } else {
            i++;
        }
    }

    // set the values of indexes from zeroCount to numsSize to 0
    for (int j = zeroCount + 1; j < numsSize; j++) {
        nums[j] = 0;
    }
}

int main() {
    int nums[5] = {0,1,0,3,12};
    moveZeroes(nums, 5);

    return 0;
}