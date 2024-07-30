#!/usr/bin/node

const request = require('request');

const characterId = 18;
const filmUrl = process.argv[2];
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(filmUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = body.results;
    const counter = films.filter(film => film.characters.includes(characterUrl)).length;

    console.log(counter);
  }
});
