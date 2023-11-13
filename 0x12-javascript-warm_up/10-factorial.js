#!/usr/bin/node
const num = Number(process.argv[2]);
const fact = number => (number === 0 || isNaN(number)) ? 1 : number * fact(number - 1);
if (num >= 0 || isNaN(num)) { console.log(fact(num)); }
