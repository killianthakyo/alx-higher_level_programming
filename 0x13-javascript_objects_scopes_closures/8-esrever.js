#!/usr/bin/node
/* returns the reversed version of a list */
exports.esrever = function (list) {
  const rev = [];
  for (const i in list) {
    rev.unshift(list[i]);
  }
  return (rev);
};
