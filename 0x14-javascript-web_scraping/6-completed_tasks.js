#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }

  const completed = {};
  body.forEach(e => {
    if (completed[e.userId] === undefined && e.completed) {
      completed[e.userId] = 1;
      return;
    }

    if (e.completed === true) completed[e.userId] += 1;
  });

  console.log(completed);
});
