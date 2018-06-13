/**
 * @param {string} str
 * @return {boolean}
 */
const checkRecord = function(str) {
  let numA = 0;
  let numL = 0;
  for (let i = 0; i < str.length; i++) {
    switch (str[i]) {
      case 'A':
        numA++;
        numL = 0;
        if (numA === 2) {
          return false;
        }
        break;
      case 'L':
        numL++;
        if (numL === 3) {
          return false;
        }
        break;
      default:
        numL = 0;
        break;
    }
  }

  return true;
};

const input = 'LALL';
console.log(checkRecord(input));
