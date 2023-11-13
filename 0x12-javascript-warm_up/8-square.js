#!/usr/bin/node

// a script that prints a square
//  first argument is the size of the square
//  If the first argument can’t be converted to an integer, print “Missing size”
const process = require('process');
const firstArgv = process.argv[2];
const size = parseInt(firstArgv);
if (!isNaN(size)) { for (let i = 0; i < size; i++) { let row = ''; for (let j = 0; j < size; j++) { row += 'X'; } console.log(row); } } else { console.log('Missing size'); }
