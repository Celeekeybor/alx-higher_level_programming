#!/usr/bin/node
exports.callMeMoby = function (x, fun) {
  for (let i = 0; i < x; i++) {
    fun();
  }
};
