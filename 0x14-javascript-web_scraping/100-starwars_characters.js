#!/usr/bin/node
const request = require('request');

const BASE = 'https://swapi-api.hbtn.io/api/';
const filmId = 'films/' + process.argv[2];

request(BASE + filmId, { json: true }, (err, res, body) => {
  if (err) return console.log(err);

  body.characters.forEach(e => {
    request(e, { json: true }, (err, res, body) => {
      if (err) return console.log(err);

      console.log(body.name);
    });
  });
});
