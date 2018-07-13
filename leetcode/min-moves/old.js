/**
 * @param {number[]} nums
 * @return {number}
 */
const minMoves = arr => {
  //* Check if arr is right from the start
  const allEqual = arr.every((num, i, arr) => num === arr[0]);
  if (allEqual) {
    return 0;
  }

  const length = arr.length;

  let moves = 0;
  let nums = arr;
  let max = Math.max(...nums);
  let maxIndex;
  let done = false;
  while (!done) {
    moves++;

    maxIndex = nums.indexOf(max);
    nums = nums.map((num, i) => {
      if (i !== maxIndex) {
        return num + 1;
      }

      return num;
    });

    const sum = nums.reduce((a, num) => a + num);
    max = Math.max(...nums);
    if (sum / length === max) {
      done = true;
    }
  }

  return moves;
};

const nums = [1, 2, 3, 10];
console.log(minMoves(nums));
