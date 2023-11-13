#!/usr/bin/node

/* script that prints two arguments passed to it,
  in the following format: “ is ” */
const process = require('process');
const first = process.argv;
const second = process.argv;
console.log(`${first[2]} is ${second[3]}`);
