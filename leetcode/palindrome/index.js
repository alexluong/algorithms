/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = x => {
  if (x < 0) return false;

  const arr = [];
  while (x > 0) {
    arr.push(x % 10);
    x = Number.parseInt(x / 10);
  }

  const length = arr.length;
  for (let i = 0; i < length / 2; i++) {
    console.log(arr[i], arr[length - 1 - i]);
    if (arr[i] !== arr[length - 1 - i]) {
      return false;
    }
  }
  return true;
};

console.log(isPalindrome(121121));
