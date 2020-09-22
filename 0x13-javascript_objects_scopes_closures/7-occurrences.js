#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let res = 0;

  list.forEach(e => {
    if (e === searchElement) { res += 1; }
  });

  return res;
};
