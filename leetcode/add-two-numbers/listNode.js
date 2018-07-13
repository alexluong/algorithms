class ListNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }

  print() {
    if (this.next !== null) {
      process.stdout.write(`${this.val}->`);
      this.next.print();
    } else {
      process.stdout.write(`${this.val}\n`);
    }
  }
}

export default ListNode;
