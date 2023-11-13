#!/usr/bin/node

/*  script that prints My number: <first argument converted in integer>
  if the first argument can be converted to an integer: */
const process = require('process');
const firstArgv = process.argv[2];
const convertArgv = parseInt(firstArgv);
if (!isNaN(convertArgv)) { console.log(`My number: ${convertArgv}`); } else { console.log('Not a number'); }
