#!/usr/bin/node
const args = process.argv.slice(2);
const fileName = args[0];

const fs = require('fs');

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
