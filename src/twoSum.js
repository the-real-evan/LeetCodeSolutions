/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var i = 0;
    var num1 = 0;
    var num2 = 0;
    var diff = 0;
    var arrayLength = nums.length
    var found = false;
    var indices = [-1, -1]
    while (!found && i < arrayLength)
        {
            num1 = nums[i];
            diff = target - num1;
            var j = i + 1;
            for(; j < arrayLength; j++)
                {
                    if (nums[j] == diff)
                        {
                        num2 = nums[j];
                        found = true;
                        indices = [i, j];
                        }
                }
            i++;
        }
    return indices
};
