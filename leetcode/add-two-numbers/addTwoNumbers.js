import ListNode from './listNode';

const getTotal = (val1, val2, rememberVal) => {
  const val = val1 + val2 + rememberVal;
  let remember = val > 9 ? 1 : 0;
  return {
    val: val % 10,
    remember,
  };
};

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = (list1, list2) => {
  let total = getTotal(list1.val, list2.val, 0);

  let list3 = new ListNode(total.val);

  let l1 = list1.next;
  let l2 = list2.next;
  let l3 = list3;

  while (l1 !== null || l2 !== null) {
    const val1 = l1 ? l1.val : 0;
    const val2 = l2 ? l2.val : 0;

    total = getTotal(val1, val2, total.remember);

    l3.next = new ListNode(total.val);
    l3 = l3.next;

    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }

  if (total.remember) {
    l3.next = new ListNode(1);
  }

  return list3;
};

export default addTwoNumbers;
