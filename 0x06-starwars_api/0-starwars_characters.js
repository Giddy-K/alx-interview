#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, { timeout: 5000 }, (err, res, body) => {
  if (err) {
    console.error('Error fetching movie:', err.message);
    return;
  }
  const characters = JSON.parse(body).characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, { timeout: 5000 }, (err, res, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(characters.map(fetchCharacter))
    .then((names) => names.forEach((name) => console.log(name)))
    .catch((error) => console.error('Error fetching character:', error.message));
});
