#!/usr/bin/node
const myArg = process.argv[2];
let aRow;
if (Number.isInteger(parseInt(myArg))) {
  for (let i = 0; i < parseInt(myArg); i++) {
    aRow = '';
    for (let j = 0; j < parseInt(myArg); j++) {
      aRow = aRow + 'X';
    }
    console.log(`${aRow}`);
  }
} else {
  console.log('Missing size');
}
