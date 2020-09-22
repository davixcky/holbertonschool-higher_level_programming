#!/usr/bin/node
const request = require('request');

const BASE_URL = 'https://swapi-api.hbtn.io/api/films/';
const URL = BASE_URL + process.argv[2];

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.title);
});
