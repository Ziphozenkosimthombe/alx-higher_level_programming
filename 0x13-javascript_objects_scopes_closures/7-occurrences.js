#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let y = 0;
  list.forEach(i => searchElement === i ? y++ : y);
  return y;
};
