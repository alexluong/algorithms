const reverse = list => {
  let reversedList = list;
  let current = null;
  let next;
  while (reversedList.next !== null) {
    next = reversedList.next;
    reversedList.next = current;
    current = reversedList;
    reversedList = next;
  }
  reversedList.next = current;
  return reversedList;
};

const isPalindrome = list => {
  //* Get number of nodes
  let num = 0;

  let running = list;
  while (running !== null) {
    num++;
    running = running.next;
  }

  if (num === 0 || num === 1) {
    return true;
  }

  //* Get first half + middle node pointer
  let firstHalf = list;
  const even = num % 2 === 0;
  const lastOfFirstHalf = Math.floor(num / 2 - 1);
  running = list;
  for (let i = 0; i < lastOfFirstHalf; i++) {
    running = running.next;
  }
  let next = running.next;
  running.next = null;
  running = next;
  let middle;
  if (!even) {
    middle = running;
    running = running.next;
  }

  //* Reverse the second half
  let secondHalf = reverse(running);

  //* Compare first and last half
  let first = firstHalf;
  let last = secondHalf;
  while (first && last) {
    if (first.val !== last.val) {
      return false;
    }
    first = first.next;
    last = last.next;
  }

  //* Reverse second half again
  secondHalf = reverse(secondHalf);

  //* Put back the list
  running = firstHalf;
  let isRunningFirst = true;
  while (running !== null) {
    if (!running.next && isRunningFirst) {
      isRunningFirst = false;
      if (!even) {
        middle.next = secondHalf;
        running.next = middle;
      } else {
        running.next = secondHalf;
      }
      running = secondHalf;
    }
    running = running.next;
  }
  list = firstHalf; //* Now list is back to the original list

  return true;
};

export default isPalindrome;
