#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

// if (!url) {
//   console.error('Usage: ./status_code.js <URL>');
//   process.exit(1);
// }

request(url, (error, response) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
