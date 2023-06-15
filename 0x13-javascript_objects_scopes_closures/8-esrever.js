#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let j = 0;
  for (let i = list.length; i > 0; i--) {
    newList[j] = list[i - 1];
    j++;
  }
  return newList;
};
