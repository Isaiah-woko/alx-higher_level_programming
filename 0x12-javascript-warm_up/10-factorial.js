#!/usr/bin/node
function ComputeFactorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * ComputeFactorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);
const result = ComputeFactorial(num);
console.log(result);
