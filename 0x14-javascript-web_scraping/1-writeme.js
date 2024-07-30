#!/usr/bin/node
const args = process.argv.slice(2);
const fileName = args[0];
const content = args[1];

const fs = require('fs');

fs.writeFile(fileName, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
