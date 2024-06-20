#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  let result = '';
  for (let i = 2; process.argv[i] !== undefined; i++) {
    result += process.argv[i] + ' ';
  }
  console.log(result);
}
