import ListNode from './linked-list';
import isPalindrome from './isPalindrome';

const list = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
list.print();

console.log(isPalindrome(list));
