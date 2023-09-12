#!/usr/bin/node

const SquarePar = require('./5-square.js');

module.exports = class Square extends SquarePar {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
