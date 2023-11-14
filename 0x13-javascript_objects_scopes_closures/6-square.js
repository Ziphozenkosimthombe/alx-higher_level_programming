#!/usr/bin/node
const Sqre = require('./5-square');

class Square extends Sqre {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    console.log(
      (c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1)
    );
  }
}
module.exports = Square;
