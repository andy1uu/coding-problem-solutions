function twoSum(nums: number[], target: number): number[] {
    const differences = new Map();

    for (let i = 0; i < nums.length; i++) {
        let difference = target - nums[i];

        if (differences.has(difference)) {
            return [differences.get(difference), i];
        }

        differences.set(nums[i], i);
    }
};