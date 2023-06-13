#!/usr/bin/node
const noArgs = process.argv.length - 2;
if (noArgs === 0) {
  console.log('No argument');
} else if (noArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
