#!/usr/bin/node
const arg2 = parseInt(process.argv[2]);
if (isNaN(arg2)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg2);
}
