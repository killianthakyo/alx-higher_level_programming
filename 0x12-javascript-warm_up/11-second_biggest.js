#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments
const myVar = process.argv;
myVar.splice(0, 2);
if (isNaN(myVar[0]) || isNaN(myVar[1])) {
  console.log(0);
} else {
  myVar.sort(function (a, b) { return b - a; });
  console.log(parseInt(myVar[1]));
}
