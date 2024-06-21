#!/usr/bin/node
exports.esrever = function (list) {
  for (let left = 0, right = list.length - 1; left < right; left++, right--) {
    const temp = list[left];
    list[left] = list[right];
    list[right] = temp;
  }
  return list;
};
