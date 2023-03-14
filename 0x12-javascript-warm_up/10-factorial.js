#!/usr/bin/node
// This script computes and prints a factorial
const myVar = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
if (isNaN(myVar)) {
  console.log('1');
} else {
  console.log(factorial(myVar));
}
