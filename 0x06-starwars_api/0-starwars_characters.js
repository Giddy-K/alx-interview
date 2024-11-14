#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Parse movie information and retrieve characters list
  const characters = JSON.parse(body).characters;

  // Request each character's information in order
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });
  };

  // Use Promise.all to fetch all characters in parallel
  Promise.all(characters.map(fetchCharacter))
    .then((names) => names.forEach((name) => console.log(name)))
    .catch((error) => console.error('Failed to retrieve characters:', error));
});
