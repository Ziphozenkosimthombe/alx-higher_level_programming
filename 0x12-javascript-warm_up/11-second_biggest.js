#!/usr/bin/node
const scndBiggest = process.argv.slice(2).map(Number).sort((a, b) => b - a)[1];
console.log(scndBiggest === undefined ? 0 : scndBiggest);
