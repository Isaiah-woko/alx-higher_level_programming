#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const url2 = `${url}${movieId}/`;

request(url2, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    if (body.characters && body.characters.length > 0) {
      body.characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (err0, repos0, body0) => {
          if (err0) {
            console.log(error);
          } else if (repos0.statusCode === 200) {
            console.log(body0.name);
          }
        });
      });
    }
  }
});
