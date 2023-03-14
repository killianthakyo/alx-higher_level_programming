#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
add(a, b);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
