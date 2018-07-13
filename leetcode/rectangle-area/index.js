/**
 * [A, B]
 * [A, D]
 * [C, D]
 * [C, B]
 */
const computeOneArea = (A, B, C, D) => {
  return (C - A) * (D - B);
};

const computeIntersect = (A, B, C, D, E, F, G, H) => {
  if (A >= G || C <= E || B >= H || D <= F) {
    return 0;
  }

  let blX, blY;
  if (E > A && E < C) {
    blX = E;
  } else {
    blX = A;
  }
  if (F > B && F < D) {
    blY = F;
  } else {
    blY = B;
  }

  let trX, trY;
  if (C > E && C < G) {
    trX = C;
  } else {
    trX = G;
  }
  if (D > F && D < H) {
    trY = D;
  } else {
    trY = H;
  }

  return computeOneArea(blX, blY, trX, trY);
};

/**
 * @param {number} A
 * @param {number} B
 * @param {number} C
 * @param {number} D
 * @param {number} E
 * @param {number} F
 * @param {number} G
 * @param {number} H
 * @return {number}
 */
const computeArea = (A, B, C, D, E, F, G, H) => {
  const first = computeOneArea(A, B, C, D);
  const second = computeOneArea(E, F, G, H);
  const intersect = computeIntersect(A, B, C, D, E, F, G, H);
  return first + second - intersect;
};

// console.log(computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
// console.log(computeArea(-2, -2, 2, 2, 2, 2, 3, 3));
console.log(computeArea(-2, -2, 2, 2, 2, -2, 4, 2));
