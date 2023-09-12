#!/usr/bin/node

const sqrSize = parseInt(process.argv[2]);

if (sqrSize) {
  for (let i = 0; i < sqrSize; i++) {
    console.log('X'.repeat(sqrSize));
  }
} else {
  console.log('Missing size');
}
