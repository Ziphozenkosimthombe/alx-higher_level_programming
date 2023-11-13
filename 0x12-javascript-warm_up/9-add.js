#!/usr/bin/node

// script that prints the addition of 2 integers
// first argument is the first integer
// second argument is the second integer
const process = require('process');
const firstArgv = parseInt(process.argv[2]);
const secondArgv = parseInt(process.argv[3]);

const add = (a, b) => a + b;
console.log(add(firstArgv, secondArgv));
