#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filename = process.argv[3];

request(URL, (err, res, body) => {
  if (err) { return console.log(err); }

  fs.writeFile(filename, body, err => {
    if (err) return console.log(err);
  });
});
