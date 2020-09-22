#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
