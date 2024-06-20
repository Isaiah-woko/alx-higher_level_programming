#!/usr/bin/node
const num = parseInt(process.argv[2]);
const letter = 'C is fun';
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) { console.log(letter); }
} else {
  console.log('Missing number of occurrences');
}
