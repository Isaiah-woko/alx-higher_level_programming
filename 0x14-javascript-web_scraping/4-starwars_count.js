#!/usr/bin/node

const request = require('request');

const characterId = 18;
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(filmUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = body.results;
    let counter = 0;

    films.forEach(film => {
      if (film.characters.includes(characterUrl)) {
        counter++;
      }
    });

    console.log(counter);
  }
});
