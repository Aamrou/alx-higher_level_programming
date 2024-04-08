#!/usr/bin/node

console.log(factorial(parseInt(process.argv[2])));

function factorial (p1) {
  if (p1 === 0 || p1 === 1 || isNaN(p1)) { return 1; }

  return p1 * factorial(p1 - 1);
}
