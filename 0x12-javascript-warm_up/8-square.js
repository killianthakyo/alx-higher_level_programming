#!/usr/bin/node

const side = Math.floor(Number(process.argv[2]));

if (isNaN(side)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < side; i++) {
    let line = '';
    for (let j = 0; j < side; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
