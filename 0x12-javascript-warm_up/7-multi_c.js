#!/usr/bin/node

const iterNum = parseInt(process.argv[2]);

if (iterNum) {
  for (let i = 0; i < iterNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
