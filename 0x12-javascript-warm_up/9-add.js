#!/usr/bin/node
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));

function add (p1, p2) {
  return p1 + p2;
}
