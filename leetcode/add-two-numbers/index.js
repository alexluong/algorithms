import ListNode from './listNode';
import addTwoNumbers from './addTwoNumbers';

// const l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
// const l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

const l1 = new ListNode(1, new ListNode(8));
const l2 = new ListNode(0);
addTwoNumbers(l1, l2).print();
