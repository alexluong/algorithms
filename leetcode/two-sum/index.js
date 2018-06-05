const twoSum = (nums, target) => {
  const hash = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;

    if (typeof hash[complement] !== 'undefined') {
      return [hash[complement], i];
    }

    hash[num] = i;
  }

  return [];
};

const val = twoSum([2, 7, 11, 15], 9);
console.log(val);
