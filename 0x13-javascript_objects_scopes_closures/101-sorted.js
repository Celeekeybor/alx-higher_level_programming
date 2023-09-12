#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

const keys = Object.values(dict).map(String);
const values = Object.keys(dict).map(String);

for (let i = 0; i < values.length; i++) {
  if (!newDict[keys[i]]) {
    newDict[keys[i]] = [];
  }

  newDict[keys[i]].push(values[i]);
}

console.log(newDict);
