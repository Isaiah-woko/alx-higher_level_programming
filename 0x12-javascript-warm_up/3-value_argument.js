#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  for (let i = 2; process.argv[i] !== undefined; i++) {
    console.log(process.argv[i]);
  }
}
