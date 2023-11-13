#!/usr/bin/node

// script that prints x times “C is fun”
// If the first argument can’t be converted to an integer, print
// “Missing number of occurrences”
const process = require('process');
const firstArgv = process.argv[2];
const x = parseInt(firstArgv);
if (!isNaN(x)) { for (let i = 0; i < x; i++) { console.log('C is fun'); } } else { console.log('Missing number of occurrences'); }
