#!/usr/bin/node
let array;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  array = process.argv.slice(2);
  array.sort(function (a, b) { return a - b; });
  array.reverse();
  console.log(array[1]);
}
