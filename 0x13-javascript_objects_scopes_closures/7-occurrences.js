#!/usr/bin/node
/* returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let aux = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      aux++;
    }
  }
  return (aux);
};
