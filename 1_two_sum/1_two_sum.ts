// # https://leetcode.com/problems/two-sum/

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Input: nums = [3,2,4], target = 6
// Output: [1,2]


function solve(nums: Array<number>, target: number) {
    let cache = {};

    for (let index in nums) {

        let valueNeeded = target - nums[index];
        
        if (valueNeeded in cache) {
            return [cache[valueNeeded], index]
        }

        let k = nums[index];

        valueNeeded[k] = index;

    }
    return [null, null];
}


console.log(solve([2, 7, 11, 15], 9));
