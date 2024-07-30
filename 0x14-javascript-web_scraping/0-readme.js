#!/usr/bin/node
const args = process.argv.slice(2);
const FileName = args[0];

const fs = require('fs');

fs.readFile(FileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
