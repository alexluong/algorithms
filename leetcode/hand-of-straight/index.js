/**
 * @param {number[]} hand
 * @param {number} W
 * @return {boolean}
 */
const isNStraightHand = (hand, W) => {
  const length = hand.length;

  //* If hand is divisible by W
  if (length % W !== 0) {
    return false;
  }

  const groups = [];
  for (let i = 0; i < length; i++) {
    const card = hand[i];

    //* Go through all existing groups
    for (let j = 0; j < groups.length; j++) {
      //* Check first in group
      if (Math.abs(groups[i][0] - card) < W) {
      }
    }
  }
};

const hand = [3, 5, 2, 1, 6, 7];
const W = 3;
console.log(isNStraightHand(hand, W));
