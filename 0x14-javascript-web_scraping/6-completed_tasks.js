#!/usr/bin/node
// print users with completed tasks
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const userTask = {};
    body.forEach(task => {
      if (task.completed) {
        if (!userTask[task.userId]) {
          userTask[task.userId] = 0;
        }
        userTask[task.userId]++;
      }
    });
    console.log(userTask);
  }
});
