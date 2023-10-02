#!/usr/bin/node
// function that returns the number of occurrences in a list
const data = require('./100-data');
const initialList = data.list;

const newList = initialList.map((value, index) => value * index);

console.log(initialList);
console.log(newList);
