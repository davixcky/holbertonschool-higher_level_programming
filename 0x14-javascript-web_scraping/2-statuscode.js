#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log('code: ' + res.statusCode);
});
