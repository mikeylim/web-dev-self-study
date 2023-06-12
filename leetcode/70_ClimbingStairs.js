// 70. Climbing Stairs
// Easy

// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2. In how many distinct ways can you climb to the top?

 

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 + 1
// 2. 2
// Example 2:               --> 0

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 + 1 + 1
// 2. 1 + 2
// 3. 2 + 1                 --> 0

// Input: n = 4
// Output: 5
// Explanation: There are five ways to climb to the top.
// 1. 1 + 1 + 1 + 1
// 2. 1 + 1 + 2
// 3. 1 + 2 + 1
// 4. 2 + 1 + 1
// 5. 2 + 2                 --> 1


// Input: n = 5
// Explanation: There are five ways to climb to the top.
// 1. 1 + 1 + 1 + 1 + 1
// 2. 1 + 1 + 1 + 2
// 3. 1 + 1 + 2 + 1
// 4. 1 + 2 + 1 + 1
// 5. 2 + 1 + 1 + 1
// 6. 2 + 2 + 1
// 7. 2 + 1 + 2                
// 8. 1 + 2 + 2                 --> 3

// Input: n = 6
// Explanation: There are five ways to climb to the top.
// 1. 1 + 1 + 1 + 1 + 1 + 1     --> totalSteps++
// 2. 1 + 1 + 1 + 1 + 2
// 3. 1 + 1 + 1 + 2 + 1
// 4. 1 + 1 + 2 + 1 + 1
// 5. 1 + 2 + 1 + 1 + 1
// 6. 2 + 1 + 1 + 1 + 1         --> n - 1
// 7. 2 + 2 + 1 + 1
// 8. 2 + 1 + 2 + 1
// 9. 2 + 1 + 1 + 2
// 10. 1 + 2 + 2 + 1
// 11. 1 + 2 + 1 + 2
// 12. 1 + 1 + 2 + 2            --> 6
// 13. 2 + 2 + 2                --> 1


/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let totalSteps = 0;
    if (n > 0)
        totalSteps++; // at least 1
    totalSteps += n-1;  // n - 1


    // n-1
    // n * 2 - 1
};