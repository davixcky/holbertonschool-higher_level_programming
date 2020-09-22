#!/usr/bin/node

exports.esrever = function (list) {
  const tmp = [];
  list.reduceRight((_, item) => tmp.push(item), null);
  return tmp;
};
