#!/usr/bin/node
const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/people' + '/18';

request(URL, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.films.length);
});
