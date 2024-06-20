#!/usr/bin/node
function compute_factorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * compute_factorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);
const result = compute_factorial(num);
console.log(result);
