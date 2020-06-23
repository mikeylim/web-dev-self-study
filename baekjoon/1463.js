function minNumOfCalculation(x) {
    let N = x;
    let M = x;
    let count1 = 0;
    let count2 = 0;

    console.log("Initially, N is: " + N);
    if (N == 1) {
        return count1;
    }

    while(true) {
        if (((N % 3) != 0) && ((N % 2) != 0) && (N !== 1)) { // if not divisible by 2 or 3 ==> minus 1 first.
            N -= 1;
            count1++;
            console.log("N is: " + N);
            console.log("count1 is: " + count1);
        } else if ((N % 3) == 0) { // while divisible by 3
            N /= 3;
            count1++;
            console.log("N is: " + N);
            console.log("count1 is: " + count1);
        } else if ((N % 2) == 0) { // while divisible by 2
            N /= 2;
            count1++;
            console.log("N is: " + N);
            console.log("count1 is: " + count1);
        } else {
            break;
        }
        // if count1 > count2 
        //  console.log(count2)
        // else 
        //  console.log (count1)
    }
    console.log("");
    console.log("Initially, M is: " + M);
    while(true) {
        if (((M % 3) != 0) && (M !== 1)) { // if not divisible by 2 or 3 ==> minus 1 first.
            M -= 1;
            count2++;
            console.log("M is: " + M);
            console.log("Count2 is: " + count2);
        } else if ((M % 3) == 0) { // while divisible by 3
            M /= 3;
            count2++;
            console.log("M is: " + M);
            console.log("Count2 is: " + count2);
        } else if ((N % 2) == 0) { // while divisible by 2
            M /= 2;
            count2++;
            console.log("M is: " + M);
            console.log("Count2 is: " + count2);
        } else {
            break;
        }
        
    }
    console.log("");

    if (count1 >= count2) {
        console.log("Better one is count2: " + count2);
        return count2;
    } else {
        console.log("count1 still wins: " + count1);
        return count1;
    }
    // console.log("FINALLY -- N is: " + N);
    // console.log("FINALLY -- count1 is: " + count1);
}
minNumOfCalculation(31); // 9 (9/3) -> 3 (3/3) -> 1 = 2
console.log("");
// minNumOfCalculation(10); // 10 (10-1) -> 9 (9/3) -> 3 (3/3) -> 1 = 3
// console.log("");
// minNumOfCalculation(12); // 12 (12/3) -> 4 (4/2) -> 2 (2-1) -> 1 = 3
// console.log("");
// minNumOfCalculation(15); // 15 (15/3) -> 5 (5-1) -> 4 (4/2) -> 2 (2-1) -> 1 = 4

// 11 -> 10 -> 9 -> 3 -> 1 = 4
// 16 -> 8 -> 4 -> 2 -> 1 = 4
// 16 -> 15 -> 5 -> 4 -> 2 -> 1 = 5
// 16 -> 15 -> 14 -> 7 -> 6 -> 3 -> 1 = 6
// 10 -> 9 -> 3 - > 1 = 3
// 10 -> 5 -> 4 -> 2 -> 1 = 4
// 13 -> 12 -> 4 -> 2 -> 1 = 4
// 13 -> 12 -> 6 -> 2 -> 1 = 4
// 21 -> 7 -> 6 -> 2 -> 1 = 4
// 26 -> 13 -> 12 -> 4 -> 2 -> 1 = 5
// 31 -> 30 -> 10 -> 9 -> 3 -> 1 = 5
// 31 -> 30 -> 10 -> 5 -> 4 -> 2-> 1 = 6



// always divide by 3 (bigger number) first