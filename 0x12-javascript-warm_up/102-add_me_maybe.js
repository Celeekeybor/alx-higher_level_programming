#!/usr/bin/node
exports.addMeMaybe = function (x, fun) {
  x += 1;
  fun(x);
};
