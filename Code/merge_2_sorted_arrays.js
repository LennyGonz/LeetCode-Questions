/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

const curry = f => x => y => f(x, y)

const concat = (x, y) => x +','+ y;

const first = xs => xs[0]

const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]

ex1 = [1, 2, 3];
ex2 = [4, 5, 6];

var mergeTwoLists = function (l1, l2) {
  let result = l1.map(function (l1_elem, l2_elem) {
    if (l1_elem < l2[l2_elem]) {
      [].concat(l1_elem)
    } else {
      [].concat(l2[l2_elem])
    }
  })
  return result;
};

console.log(mergeTwoLists(ex1, ex2));

mergeTwoLists(ex1, ex2);
