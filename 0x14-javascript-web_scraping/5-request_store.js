#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const url = args[0];
const filePath = args[1];

const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
