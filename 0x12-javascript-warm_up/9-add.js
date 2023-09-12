#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  const res = a + b;
  return res;
}

console.log(add(a, b));
