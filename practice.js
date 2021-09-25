// riskWorkflowStateArr = ["Time", "RiskchangedByPolymer", "Scope", "Hacker Angriff", "Test", "Test(2)"];
// riskNamesArr = ["In Bearbeitung", "Abgeschlossen", "In Bearbeitung", "Abgeschlossen", "Geplant", "In Bearbeitung"];

// testArr = riskNamesArr.map(function (x, i) {
//   console.log("x", x)
//   console.log("i", i)
//   return {"name": x, "state": riskWorkflowStateArr[i]}
// })

// console.log(testArr);

// ex1 = [1,2,3]
// ex2 = [4, 5, 6]

// const mergeTwoLists = function (l1, l2) {
//   for (let i = 0; i < l2.length; i++){
//     if (l1[i] <= l2[i]) {
//       l2[0].append(l1[i])
//     }
//   }
// }

// console.log(mergeTwoLists([1,2,3], [4,5,6]))

/**
 * Step 1) Know what your function should do
 *
 * Looking at our sumTo() function -> it's clear that the function SHOULD return an integer sum from 1 to n
 *
 * function sumTo(n){
 *
 * }
 */

/**
 * Step 2) Pick a subproblem and assume your function ALREADY works on it
 *
 * Our origin problem is to sum all values from 1 to n
 *
 * A subproblem in this case is to sum all numbers up to a value SMALLER than n
 *
 * If sumTo(n) was our origin problem
 * these are all considered subproblems b/c theyre smaller versions of the original
 *
 * sumTo(n-1)
 * sumTo(n-2)
 * sumTo(n-3)
 * ...
 * sumTo(1)
 *
 * Now we pick an appropriate subproblem by choosing  one as close to the original as possible
 *
 * Since we assume that sumTo() function ALREADY WORKS
 * why not pick a value that solves the bulk of the problem for us?
 *
 * In this case, since our problem solves for n, then the best subproblem should solve for n-1
 *
 * function sumTo(n) {
 * // using n-1 as our subproblem, it returns the sum from 1 to n-1
 *  const solutionToSubproblem = sumTo(n-1)
 * }
 *
 * To solve a recursion problem, let's ASSUME that the function ALREADY WORKS for any subproblem we want
 *
 * Because of our subproblem selection, we already have the sum of all values from 1 to n-1
 */

/**
 * Step 3) Take the answer to your subproblem, and use it to solve for the original problem
 *
 * We want to find the sum from 1 to n, and we already have the solution from 1 to n-1
 *
 * How do we get the sum from 1 to n, if we have the solution from 1 to n-1?
 *
 * sumTo(n-1) // 1 + 1 .... n-2 + n -1
 *
 * sumTo(n) // 1 + 2 ... n-2 + n - 1 + n
 *
 * So all we need to do is add n to the solution of our subproblem
 *
 * function sumTo(n) {
 *  const solutionToSubproblem = sumTo(n-1)
 *
 *  return solutionToSubproblem + n
 * }
 *
 * As you saw, we took the solution to our subproblem and found how it's used to solve the original problem
 *
 * This is known as finding the RECURRENCE RELATION
 */

/**
 * Step 4) You already solved 99% of the problem. The remaining 1%? Base case.
 *
 * Your funciton is calling itself, so it will probably run forever. That is why we need to add a base case to stop it
 *
 * What is a base case and how do we determine a base case?
 *
 * A base case is a way for us to stop the recursion.
 * USUALLY, it can be a simple if-else statement in the beginning of the function
 *
 * The condition prevents more function calls if it has reached its base case.
 *
 * To pick a base case, thinking of the following
 *
 * What is the EASIEST POSSIBLE VALUE you can put into the function that requires no extra calculation?
 *
 * In our case, that would be n = 0
 *
 * It's obvious that the sum of all values from 0 to 0, is 0
 * so why bother doing more recursion?
 */

/*
function sumTo(n) {
  // n is our original problem
  if (n === 0) {
    return 0;
  }
  const solutionToSubproblem = sumTo(n - 1); // n-1 is our subproblem
  return solutionToSubproblem + n;
}

console.log(sumTo(3));

function reverse(s) {
  if (s === "") {
    return "";
  } // Base case
  const subproblem = s.slice(1, s.length);
  const reversedSubproblem = reverse(subproblem);
  return reversedSubproblem + s[0];
}

console.log(reverse("hello"));

function fibo(num) {
  if (num == 0) return 0;
  if (num == 1) return 1;

  return fibo(num - 1) + fibo(num - 2);
}

console.log(fibo(4));

*/
