#!/usr/bin/node
const myArg = process.argv[2];
if (Number.isInteger(parseInt(myArg))) {
  for (let i = 0; i < parseInt(myArg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
