/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
const shortestToChar = (s, c) => {
  const arr = [];
  let oldIndex;
  let newIndex = s.indexOf(c);
  let i = 0;

  // From start to first c
  while (i <= newIndex) {
    arr[i] = newIndex - i;
    i++;
  }

  // In between
  oldIndex = newIndex;
  newIndex = s.indexOf(c, oldIndex + 1);
  while (newIndex !== -1) {
    while (i <= newIndex) {
      if (i - oldIndex > newIndex - i) {
        arr[i] = newIndex - i;
      } else {
        arr[i] = i - oldIndex;
      }
      i++;
    }
    oldIndex = newIndex;
    newIndex = s.indexOf(c, newIndex + 1);
  }

  // From last c to end
  while (i < s.length) {
    arr[i] = i - oldIndex;
    i++;
  }

  return arr;
};

const string = 'loveleetcode';
const char = 'e';
console.log(shortestToChar(string, char));
