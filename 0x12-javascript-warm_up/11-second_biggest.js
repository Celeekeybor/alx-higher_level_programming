#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arrNum = process.argv.slice(2).map(Number);
  console.log(arrNum.sort((a, b) => a - b)[arrNum.length - 2]);
}
